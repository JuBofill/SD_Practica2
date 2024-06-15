import sys
from proto import store_pb2, store_pb2_grpc


class Slave():
    def __init__(self, id):
        self.id = id
        self.data = {}
        self.delay = 0


if __name__ == "__main__":
    id = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]
    m_ip = sys.argv[4]