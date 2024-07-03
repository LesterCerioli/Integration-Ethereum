import threading
import time
from logger import log_event  # Certifique-se de que logger.py está no mesmo diretório
from currency_service import get_exchange_rate

class ExchangeRateWorker:
    def __init__(self, interval: int = 60):
        self.interval = interval
        self.stop_event = threading.Event()
    
    def start(self):
        thread = threading.Thread(target=self.run, daemon=True)
        thread.start()

    def run(self):
        while not self.stop_event.is_set():
            try:
                # Fetch exchange rates
                usd_rate = get_exchange_rate("usd")
                brl_rate = get_exchange_rate("brl")

                # Log the retrieved exchange rates
                log_event(f"USD Rate: {usd_rate}, BRL Rate: {brl_rate}")

                # Sleep for the interval duration
                time.sleep(self.interval)
            except Exception as e:
                log_event(f"Error in worker loop: {e}", level='error')

    def stop(self):
        self.stop_event.set()

if __name__ == "__main__":
    log_event("Starting the exchange rate worker")
    worker = ExchangeRateWorker(interval=60)
    worker.start()

    # Keep the main thread alive to let the worker run
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log_event("Stopping the exchange rate worker")
        worker.stop()
