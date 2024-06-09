import logging
import sys
import socket

hostname = socket.gethostname()

app_logger = logging.getLogger("app")
user_logger = logging.getLogger("user")
device_logger = logging.getLogger("device")

app_logger.setLevel(logging.DEBUG)
user_logger.setLevel(logging.DEBUG)
device_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/app.log")
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - {} - %(name)s - %(levelname)s - %(message)s'.format(hostname))

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

app_logger.addHandler(file_handler)
app_logger.addHandler(console_handler)

user_logger.addHandler(file_handler)
user_logger.addHandler(console_handler)

device_logger.addHandler(file_handler)
device_logger.addHandler(console_handler)
