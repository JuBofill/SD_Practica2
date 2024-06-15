import signal
import sys
import time
import yaml
import subprocess


# Carregar configuracio
def load_config(file):
    with open(file, 'r') as file:
        return yaml.safe_load(file)


# Iniciar proces del Master
def start_master(id, ip, port):
    return subprocess.Popen(["python3", "centralized/master.py", id, ip, str(port)])


# Iniciar proces Slave
def start_slave(id, ip, port, m_ip, m_port):
    return subprocess.Popen(["python3", "centralized/slave.py", id, ip, str(port), f"{m_ip}:{m_port}"])


# Funció per gestionar la senyal SIGINT
def signal_handler_INT(sig, frame):
    sys.exit(0)


# Funció per gestionar la senyal SIGTERM
def signal_handler_TERM(sig, frame):
    time.sleep(1)
    for process in processes:
        process.terminate()
    sys.exit(0)


if __name__ == "__main__":
    config = load_config("centralized_config.yaml")

    processes = []
    process = start_master("master", config["master"]["ip"], config["master"]["port"])

    for slave in config["slaves"]:
        process = start_slave(slave["id"], slave["ip"], slave["port"], config["master"]["ip"], config["master"]["port"])
        processes.append(process)

    signal.signal(signal.SIGINT, signal_handler_INT)
    signal.signal(signal.SIGTERM, signal_handler_TERM)

    while True:
        time.sleep(10000)
