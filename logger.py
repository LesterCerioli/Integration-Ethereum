import logging
from datetime import datetime
import pytz

# Configuração do fuso horário de Washington D.C.
washington_tz = pytz.timezone('America/New_York')

# Configuração do logger
logging.basicConfig(filename='service.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def log_event(message: str, level: str = 'info') -> None:
    current_time = datetime.now(washington_tz)
    log_message = f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} - {message}"
    if level == 'info':
        logging.info(log_message)
    elif level == 'error':
        logging.error(log_message)
    else:
        logging.warning(log_message)
