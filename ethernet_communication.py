# ethernet_communication.py
import threading
import socket
import logging

class EthernetCommunication(threading.Thread):
    def __init__(self, ip, port):
        super().__init__()
        self.server_address = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        self.logger = logging.getLogger("AuxiliaryLogger")
        self.logger.debug(f"Initialized EthernetCommunication with IP={ip}, port={port}")

    def run(self):
        self.logger.info("Ethernet communication thread started.")
        try:
            self.sock.connect(self.server_address)
            self.logger.info(f"Connected to Ethernet server at {self.server_address}")
            while self.running:
                data = self.sock.recv(1024)
                if data:
                    self.logger.debug(f"Received Ethernet data: {data}")
                    # Process the data as needed
        except Exception as e:
            self.logger.error(f"Ethernet communication error: {e}")
        finally:
            self.sock.close()
            self.logger.info("Ethernet communication thread stopped.")

    def send_data(self, data):
        try:
            self.sock.sendall(data)
            self.logger.debug(f"Sent Ethernet data: {data}")
        except Exception as e:
            self.logger.error(f"Ethernet send error: {e}")

    def stop(self):
        self.running = False
        self.sock.close()
        self.logger.info("Stopped Ethernet communication.")
