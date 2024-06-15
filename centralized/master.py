import sys
from proto import store_pb2, store_pb2_grpc


class Master():
    def __init__(self, id):
        self.id = id
        self.data = {}
        self.delay = 0
        self.slaves = {}


if __name__ == "__main__":
    id = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]