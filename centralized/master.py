import signal
import sys
import threading
import time
import grpc
from concurrent import futures
from proto import store_pb2, store_pb2_grpc
from node import Node


# Classe Master
class Master(Node):
    def __init__(self, id):
        super().__init__(id)
        self.slaves = {}

    # Put
    def put(self, request, context):
        key = request.key
        value = request.value

        # 2PC
        self.log("Starting 2PC")
        can_commit = True
        for slave_address, slave_stub in self.slaves.items():
            try:
                response = slave_stub.canCommit(store_pb2.CommitRequest(key=key, value=value))
                if not response.can_commit:
                    can_commit = False
                    break
            except grpc.RpcError as e:
                self.log(f"Error connecting to slave")

        if can_commit:
            threading.Thread(target=self.do_commit, args=(key, value,)).start()
            self.lock.acquire()
            self.data[key] = value
            self.lock.release()
        else:
            print("2PC failed")

        time.sleep(self.delay)
        return store_pb2.PutResponse(success=can_commit)

    # Confirmar commit
    def do_commit(self, key, value):
        for slave_address, slave_stub in self.slaves.items():
            try:
                slave_stub.doCommit(store_pb2.CommitRequest(key=key, value=value))
            except grpc.RpcError as e:
                self.log(f"Error connecting to slave while committing")

    # Registrar Slave
    def registerSlave(self, request, context):
        slave_address = request.address
        channel = grpc.insecure_channel(slave_address)
        slave_stub = store_pb2_grpc.KeyValueStoreStub(channel)
        self.slaves[slave_address] = slave_stub
        self.log(f"Registered slave {slave_address}")
        return store_pb2.RegisterSlaveResponse(success=True, state=self.data)


# Servidor gRPC
def serve(id, ip, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(Master(id), server)
    server.add_insecure_port(f"{ip}:{port}")
    server.start()
    print(f"Master running on port {port}")

    # Funcio per gestionar les senyals SIGINT i SIGTERM
    def signal_handler(sig, frame):
        print(f"Stopping {id}...")
        server.stop(0)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        time.sleep(10000)


if __name__ == "__main__":
    id = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]

    serve(id, ip, port)
