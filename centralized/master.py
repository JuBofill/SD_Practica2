import signal
import sys
import time

import grpc
from concurrent import futures
from proto import store_pb2, store_pb2_grpc


# Classe Master
class Master():
    def __init__(self, id):
        self.id = id
        self.data = {}
        self.delay = 0
        self.slaves = {}


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
