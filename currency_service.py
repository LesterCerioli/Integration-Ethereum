import requests
import time
from config import COINGECKO_API_URL
import logging

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("currency_service.log"),
        logging.StreamHandler()
    ]
)

def log_event(message: str, level: str = 'info'):
    if level == 'error':
        logging.error(message)
    else:
        logging.info(message)

def get_exchange_rate(currency: str) -> float:
    try:
        response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids=ethereum&vs_currencies={currency}")
        response.raise_for_status()
        data = response.json()
        rate = data['ethereum'][currency]
        log_event(f"Successfully retrieved exchange rate for {currency}: {rate}")
        return rate
    except Exception as e:
        log_event(f"Failed to retrieve exchange rate for {currency}: {e}", level='error')
        raise

# Exemplo de uso da função
if __name__ == "__main__":
    while True:
        try:
            # Fetch and log the exchange rate for USD and BRL
            usd_rate = get_exchange_rate("usd")
            brl_rate = get_exchange_rate("brl")
            log_event(f"USD Rate: {usd_rate}, BRL Rate: {brl_rate}")

            # Sleep for 3 minutes (180 seconds)
            time.sleep(180)
        except Exception as e:
            log_event(f"Error in main loop: {e}", level='error')
            log_event("Retrying in 5 seconds...", level='info')
            time.sleep(5)
