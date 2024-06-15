import json
import signal
import subprocess
import sys
import time

import yaml


# Carregar configuracio
def load_config(file):
    with open(file, 'r') as file:
        return yaml.safe_load(file)


def start_node(id, ip, port, weight, nodes, read_size, write_size):
    return subprocess.Popen(
        ["python3", "decentralized/node.py", id, ip, str(port), str(weight), json.dumps(nodes), str(read_size),
         str(write_size)])


# Funcio per gestionar la senyal SIGINT
def signal_handler_INT(sig, frame):
    sys.exit(0)


# Funcio per gestionar la senyal SIGTERM
def signal_handler_TERM(sig, frame):
    time.sleep(1)
    for process in processes:
        process.terminate()
    sys.exit(0)


if __name__ == "__main__":
    config = load_config("decentralized_config.yaml")

    processes = []
    nodes = []

    write_size = 3
    read_size = 2

    for n in config["nodes"]:
        n_ip = n["ip"]
        n_port = n["port"]
        process = start_node(n["id"], n["ip"], n["port"], n["weight"], nodes, read_size, write_size)
        processes.append(process)
        nodes.append(f"{n_ip}:{n_port}")

    # Assignar el gestor de senyals per SIGINT i SIGTERM
    signal.signal(signal.SIGINT, signal_handler_INT)
    signal.signal(signal.SIGTERM, signal_handler_TERM)

    # Bucle infinit
    while True:
        time.sleep(10000)
