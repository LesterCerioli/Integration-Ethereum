import logging
import json
from logging.handlers import RotatingFileHandler

# Definição do formato JSON para os logs
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "lineno": record.lineno,
            "pathname": record.pathname
        }
        return json.dumps(log_entry)

# Configuração do logger
file_handler = RotatingFileHandler("currency_service.log", maxBytes=2000000, backupCount=5)
file_handler.setFormatter(JsonFormatter())
