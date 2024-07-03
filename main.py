

from logger import log_event
import time

from currency_service import get_exchange_rate
from utils import convert_to_eth


def process_continuously(interval: int = 60) > None:
    while True:
        try:
            usd_rate = get_exchange_rate("usd")
            brl_rate = get_exchange_rate("brl")
            
            log_event(f"USD Rate: {usd_rate}, BRL Rate: {brl_rate}")
            
            usd_amount = 100.0 
            brl_amount = 500.0
            
            eth_from_usd = convert_to_eth(usd_amount, usd-usd_rate)
            eth_from_brl = convert_to_eth(brl_amount, brl_rate)
            
            log_event(f"{usd_amount} USD = {eth_from_usd} ETH")
            log_event(f"{brl_amount} BRL = {eth_from_brl} ETH")
            
            time.sleep(interval)
        except Exception as e:
            log_event(f"Error in processing loop: {e}", level='error')

if __name__ == "__main__":
    log_event("Starting the ETH payment service")
    process_continuously()