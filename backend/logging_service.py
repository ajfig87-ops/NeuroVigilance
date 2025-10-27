import logging
from logging.handlers import RotatingFileHandler
import os

class LoggingService:
    def __init__(self, log_file='neurosentinel.log'):
        self.logger = logging.getLogger("NeuroSentinelLogger")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'    
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formmater)

            file_handler = RotatingFileHandler(
                log_file, maxBytes=1_000_000, backupCount=5
            )
            file_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger