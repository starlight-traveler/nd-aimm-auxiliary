# config.py
import logging
import logging.config
import yaml
import os
import sys

class Config:
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()
        self.setup_logging()
        self.logger = self.get_logging_logger("AuxiliaryLogger")
        self.log_startup_time()

    def load_config(self):
        if not os.path.exists(self.config_path):
            print(f"Configuration file {self.config_path} not found.")
            sys.exit(1)
        
        with open(self.config_path, 'r') as f:
            try:
                config = yaml.safe_load(f)
                return config
            except yaml.YAMLError as e:
                print(f"Error parsing the configuration file: {e}")
                sys.exit(1)

    def setup_logging(self):
        logging_config = self.config.get('logging')
        if not logging_config:
            print("Logging configuration not found in config.yaml.")
            sys.exit(1)
        
        # Ensure the log directory exists
        log_file = logging_config['handlers']['file']['filename']
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
                print(f"Created log directory: {log_dir}")
            except Exception as e:
                print(f"Failed to create log directory {log_dir}: {e}")
                sys.exit(1)
        
        # Configure logging
        try:
            logging.config.dictConfig(logging_config)
        except Exception as e:
            print(f"Failed to configure logging: {e}")
            sys.exit(1)

    def get_logging_logger(self, logger_name="DroneLogger"):
        return logging.getLogger(logger_name)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def log_startup_time(self):
        """
        Logs a startup message with a timestamp to differentiate between different startups.
        """
        self.logger.info("=========================")
