# main.py
from config import Config
from sensor_manager import SensorManager
import sys
import time

def main():
    # Initialize configuration
    config = Config(config_path='start/config.yaml')
    
    # Get the configured logger
    logger = config.get_logging_logger("AuxiliaryLogger")
    logger.info("Application started.")

    # Extract necessary configurations
    try:
        uart_config = config.get('interconnect')  # Update the key if different
        uart_port = uart_config['port']
        uart_baudrate = uart_config['baudrate']
    except KeyError as e:
        logger.error(f"Missing UART configuration: {e}")
        sys.exit(1)

    try:
        ethernet_config = config.get('ethernet')
        ethernet_ip = ethernet_config['ip']
        ethernet_port = ethernet_config['port']
    except KeyError as e:
        logger.error(f"Missing Ethernet configuration: {e}")
        sys.exit(1)

    # Initialize SensorManager with configurations
    manager = SensorManager(uart_port, uart_baudrate, ethernet_ip, ethernet_port)
    manager.start()
    logger.info("Sensor Manager started successfully.")

    try:
        while True:
            # Keep the main thread alive
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received. Shutting down.")
        manager.stop()
        logger.info("Application stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
