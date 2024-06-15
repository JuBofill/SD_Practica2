import threading
import time
from proto import store_pb2, store_pb2_grpc


# Classe Node (pare de Master i Slaves)
class Node(store_pb2_grpc.KeyValueStoreServicer):

    def __init__(self, id):
        self.id = id
        self.data = {}
        self.delay = 0
        self.lock = threading.Lock()

    # Put
    def put(self, request, context):
        pass

    # Get
    def get(self, request, context):
        key = request.key
        found = key in self.data
        self.lock.acquire()
        value = self.data.get(key, "")
        self.lock.release()
        self.log(f"GET key={key} value={value}")
        time.sleep(self.delay)
        return store_pb2.GetResponse(value=value, found=found)

    # Afegir Delay
    def slowDown(self, request, context):
        self.delay = request.seconds
        self.log(f"Delayed {self.delay} sec")
        return store_pb2.SlowDownResponse(success=True)

    # Reset Delay
    def restore(self, request, context):
        self.delay = 0
        self.log(f"delay restored")
        return store_pb2.SlowDownResponse(success=True)

    # Resposta 2PC
    def canCommit(self, request, context):
        pass

    # Confirmacio 2PC
    def doCommit(self, request, context):
        pass

    # Logs
    def log(self, msg):
        print(f"[{self.id}] {msg}")
