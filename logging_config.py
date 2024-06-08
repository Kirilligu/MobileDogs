import logging
import socket
from logging.handlers import RotatingFileHandler
import os
hostname = socket.gethostname()

if not os.path.exists('logs'):
    os.makedirs('logs')

def setup_logger(logger_name, log_file, level=logging.INFO):
    log_formatter = logging.Formatter(f'%(asctime)s - {hostname} - %(levelname)s - %(message)s')
    log_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
    log_handler.setFormatter(log_formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(log_handler)
    logger.addHandler(console_handler)
    return logger

app_logger = setup_logger('app_logger', 'logs/app.log')
user_logger = setup_logger('user_logger', 'logs/user.log')
device_logger = setup_logger('device_logger', 'logs/device.log')
