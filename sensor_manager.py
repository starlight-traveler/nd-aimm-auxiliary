# sensor_manager.py
import logging
from uart_communication import UARTCommunication
from ethernet_communication import EthernetCommunication

class SensorManager:
    def __init__(self, uart_port, uart_baudrate, ethernet_ip, ethernet_port):
        self.logger = logging.getLogger("AuxiliaryLogger")
        self.logger.debug("Initializing SensorManager.")
        self.uart_comm = UARTCommunication(uart_port, uart_baudrate)
        self.eth_comm = EthernetCommunication(ethernet_ip, ethernet_port)

    def start(self):
        self.logger.info("Starting UART and Ethernet communication threads.")
        self.uart_comm.start()
        self.eth_comm.start()

    def stop(self):
        self.logger.info("Stopping UART and Ethernet communication threads.")
        self.uart_comm.stop()
        self.eth_comm.stop()
        self.uart_comm.join()
        self.eth_comm.join()
        self.logger.info("All communication threads have been stopped.")
