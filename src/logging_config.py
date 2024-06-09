import logging
import sys
import socket
from datetime import datetime
from elasticsearch import Elasticsearch

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

# Elasticsearch setup
es = Elasticsearch(["http://localhost:9200"])

class ElasticsearchHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        es.index(index="logs", body={
            "@timestamp": datetime.utcnow().isoformat(),
            "hostname": hostname,
            "level": record.levelname,
            "message": log_entry,
            "logger": record.name
        })

# Create and set Elasticsearch handler
es_handler = ElasticsearchHandler()
es_handler.setLevel(logging.DEBUG)
es_handler.setFormatter(formatter)

# Add Elasticsearch handler to the loggers
app_logger.addHandler(es_handler)
user_logger.addHandler(es_handler)
device_logger.addHandler(es_handler)
