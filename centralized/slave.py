import signal
import sys
import time
import grpc
from concurrent import futures
from proto import store_pb2, store_pb2_grpc
from node import Node


# Classe Slave
class Slave(Node):
    def __init__(self, id, state):
        super().__init__(id)
        self.data = dict(state)

    # Resposta 2PC
    def canCommit(self, request, context):
        self.log("2PC can commit")
        time.sleep(self.delay)
        return store_pb2.CommitResponse(can_commit=True)


    # Confirmacio 2PC
    def doCommit(self, request, context):
        key = request.key
        value = request.value
        self.lock.acquire()
        self.data[key] = value
        self.lock.release()
        self.log(f"PUT key={key} value={value}")
        time.sleep(self.delay)
        return store_pb2.Empty()


# Registrar al Master
def register_to_master(master_address, slave_address):
    channel = grpc.insecure_channel(master_address)
    stub = store_pb2_grpc.KeyValueStoreStub(channel)
    response = stub.registerSlave(store_pb2.RegisterSlaveRequest(address=slave_address))
    if response.success:
        print(f"Slave {slave_address} registered to Master {master_address}")
        return response.state
    else:
        print(f"Slave {slave_address} didn't register to Master {master_address}")
        sys.exit(1)


# Servidor gRPC
def serve(id, ip, port, m_ip):
    slave_address = f"{ip}:{port}"
    state = register_to_master(m_ip, slave_address)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(Slave(id, state), server)
    server.add_insecure_port(f"{ip}:{port}")
    server.start()
    print(f"Slave running on port {port}")

    # Funcio per gestionar els senyals SIGINT i SIGTERM
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
    m_ip = sys.argv[4]

    serve(id, ip, port, m_ip)