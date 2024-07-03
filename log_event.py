import requests
import time
import logging
import json
from logging.handlers import RotatingFileHandler
from config import COINGECKO_API_URL

# Configuração do logger
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_entry)

# Definindo o handler de arquivo rotativo com formatação JSON
file_handler = RotatingFileHandler("currency_service.log", maxBytes=2000000, backupCount=5)
file_handler.setFormatter(JsonFormatter())

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler]
)

# Função para obter a taxa de câmbio
def get_exchange_rate(currency: str) -> float:
    while True:
        try:
            response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids=ethereum&vs_currencies={currency}")
            response.raise_for_status()
            data = response.json()
            rate = data['ethereum'][currency]
            log_event(f"Successfully retrieved exchange rate for {currency}: {rate}")
            return rate
        except Exception as e:
            log_event(f"Failed to retrieve exchange rate for {currency}: {e}", level='error')
            log_event("Retrying in 5 seconds...", level='info')
            time.sleep(5)

# Função para logar eventos
def log_event(message: str, level: str = 'info'):
    if level == 'error':
        logging.error(message)
    else:
        logging.info(message)

# Exemplo de uso da função
if __name__ == "__main__":
    currency = "usd"
    rate = get_exchange_rate(currency)
    print(f"The exchange rate for Ethereum in {currency} is {rate}")
