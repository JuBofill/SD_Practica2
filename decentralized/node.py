import json
import sys

from proto import store_pb2_grpc, store_pb2

# Classe Node
class Node(store_pb2_grpc.KeyValueStoreServicer):
    def __init__(self, id, weight, read_weight, write_weight, state):
        self.id = id
        self.weight = weight
        self.data = dict(state)
        self.delay = 0
        self.other_nodes = {}
        self.read_weight = read_weight
        self.write_weight = write_weight


if __name__ == "__main__":
    id = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]
    weight = int(sys.argv[4])
    ant_nodes = json.loads(sys.argv[5])
    read_weight = int(sys.argv[6])
    write_weight = int(sys.argv[7])
