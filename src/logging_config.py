import logging
import sys
import socket
from datetime import datetime
from elasticsearch import Elasticsearch

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

es_handler = ElasticsearchHandler()
es_handler.setLevel(logging.DEBUG)
es_handler.setFormatter(formatter)

app_logger.addHandler(es_handler)
user_logger.addHandler(es_handler)
device_logger.addHandler(es_handler)
