# uart_communication.py
import threading
import serial
import logging

class UARTCommunication(threading.Thread):
    def __init__(self, port, baudrate):
        super().__init__()
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.running = True
        self.logger = logging.getLogger("AuxiliaryLogger")
        self.logger.debug(f"Initialized UARTCommunication with port={port}, baudrate={baudrate}")

    def run(self):
        self.logger.info("UART communication thread started.")
        while self.running:
            try:
                if self.ser.in_waiting > 0:
                    data = self.ser.read(self.ser.in_waiting)
                    self.logger.debug(f"Received data: {data}")
                    # Process the data as needed
            except Exception as e:
                self.logger.error(f"UART read error: {e}")

    def send_data(self, data):
        try:
            self.ser.write(data)
            self.logger.debug(f"Sent data: {data}")
        except Exception as e:
            self.logger.error(f"UART send error: {e}")

    def stop(self):
        self.running = False
        self.ser.close()
        self.logger.info("UART communication thread stopped.")
