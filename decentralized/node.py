import json
import signal
import sys
import threading
import time
from concurrent import futures

import grpc

from proto import store_pb2_grpc, store_pb2

# Classe Node
class Node(store_pb2_grpc.KeyValueStoreServicer):
    def __init__(self, id, weight, read_size, write_size, state):
        self.id = id
        self.weight = weight
        self.data = dict(state)
        self.delay = 0
        self.other_nodes = {}
        self.read_size = read_size
        self.write_size = write_size

    # Get
    def get(self, request, context):
        key = request.key

        size = self.quorum(key)
        if size >= self.read_size:
            self.log(f"Quorum succeded on GET. Required={self.read_size}, Obtained={size}")
            value = self.data.get(key, "")
            found = key in self.data
            self.log(f"GET key={key} value={value}")
            time.sleep(self.delay)
            return store_pb2.GetResponse(value=value, found=found)
        else:
            self.log(f"Quorum failed on GET. Required={self.read_size}, Obtained={size}")
            time.sleep(self.delay)
            return store_pb2.GetResponse(value="", found=False)

    # Put
    def put(self, request, context):
        key = request.key
        value = request.value

        size = self.quorum(key)
        if size >= self.write_size:
            self.log(f"Quorum succeded on PUT. Required={self.write_size}, Obtained={size}")
            threading.Thread(target=self.do_commit, args=(key, value,)).start()
            self.data[key] = value
            self.log(f"PUT key={key} value={value}")
            time.sleep(self.delay)
            return store_pb2.PutResponse(success=True)
        else:
            self.log(f"Quorum failed on PUT. Required={self.write_size}, Obtained={size}")
            time.sleep(self.delay)
            return store_pb2.PutResponse(success=False)

    # Confirmacio Quorum
    def do_commit(self, key, value):
        for other_address, other_stub in self.other_nodes.items():
            try:
                other_stub.doCommit(store_pb2.CommitRequest(key=key, value=value))
            except grpc.RpcError as e:
                self.log(f"Error connecting to node while committing")

    # Quorum
    def quorum(self, key):
        self.log("Starting Quorum")

        # Votacio
        size = 0
        for other_address, other_stub in self.other_nodes.items():
            try:
                response = other_stub.askVote(store_pb2.AskVoteRequest(key=key))
                size += response.weight
            except grpc.RpcError as e:
                self.log(f"Error connecting to node while voting")

        return size + self.weight

    # Confirmar commit
    def doCommit(self, request, context):
        key = request.key
        value = request.value
        self.data[key] = value
        self.log(f"PUT key={key} value={value}")
        time.sleep(self.delay)
        return store_pb2.Empty()

    # Afegir Delay
    def slowDown(self, request, context):
        self.delay = request.seconds
        self.log(f"Delayed {self.delay} sec")
        return store_pb2.SlowDownResponse(success=True)

    # Reset Delay
    def restore(self, request, context):
        self.delay = 0
        self.log(f"Delay restored")
        return store_pb2.SlowDownResponse(success=True)

    # Registrar Node
    def registerNode(self, request, context):
        other_address = request.address
        channel = grpc.insecure_channel(other_address)
        other_stub = store_pb2_grpc.KeyValueStoreStub(channel)
        self.other_nodes[other_address] = other_stub
        self.log(f"Registered node {other_address}")
        return store_pb2.RegisterNodeResponse(success=True, state=self.data)

    # Enviar pes durant el Quorum
    def askVote(self, request, context):
        time.sleep(self.delay)
        return store_pb2.AskVoteResponse(weight=self.weight)

    # Logs
    def log(self, msg):
        print(f"[{self.id}] {msg}")


# Registrar-se als altres nodes
def register_to_node(other_address, my_address):
    while True:
        try:
            channel = grpc.insecure_channel(other_address)
            stub = store_pb2_grpc.KeyValueStoreStub(channel)
            response = stub.registerNode(store_pb2.RegisterNodeRequest(address=my_address))
            if response.success:
                print(f"Node {my_address} registered to Node {other_address}")
                return response.state
            else:
                print(f"Node {my_address} didn't register to Node {other_address}")
                sys.exit(1)
        except grpc._channel._InactiveRpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                time.sleep(.5)
            else:
                raise e


# Servidor gRPC
def serve(id, ip, port, weight, other_nodes, read_size, write_size):
    my_address = f"{ip}:{port}"
    state = {}

    # Registrar node actual als altres nodes
    for other in other_nodes:
        state = register_to_node(other, my_address)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(Node(id, weight, read_size, write_size, state), server)
    server.add_insecure_port(f"{ip}:{port}")
    server.start()
    print(f"Node listening to port {port}...")

    # Registrar altres nodes al node actual
    for other in other_nodes:
        register_to_node(my_address, other)

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
    weight = int(sys.argv[4])
    ant_nodes = json.loads(sys.argv[5])
    read_size = int(sys.argv[6])
    write_size = int(sys.argv[7])
    serve(id, ip, port, weight, ant_nodes, read_size, write_size)
