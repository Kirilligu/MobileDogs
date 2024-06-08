import logging
import sys
import socket

# Get the hostname of the machine
hostname = socket.gethostname()

# Create custom loggers for different parts of the application
app_logger = logging.getLogger("app")
user_logger = logging.getLogger("user")
device_logger = logging.getLogger("device")

# Set the logging level for each logger
app_logger.setLevel(logging.DEBUG)
user_logger.setLevel(logging.DEBUG)
device_logger.setLevel(logging.DEBUG)

# Create handlers for logging to file and console
file_handler = logging.FileHandler("logs/app.log")
console_handler = logging.StreamHandler(sys.stdout)

# Create a formatter with time, hostname, and log level
formatter = logging.Formatter('%(asctime)s - {} - %(name)s - %(levelname)s - %(message)s'.format(hostname))

# Set the formatter for handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the loggers
app_logger.addHandler(file_handler)
app_logger.addHandler(console_handler)

user_logger.addHandler(file_handler)
user_logger.addHandler(console_handler)

device_logger.addHandler(file_handler)
device_logger.addHandler(console_handler)
