import logging
from logging import DEBUG

f_handler = logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("_____%(asctime)s - %(levelname)s - %(message)s_____"))

# Налаштування конфігурації логування
# logging.basicConfig(level=logging.ERROR,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),
                        f_handler
                    ], force=True)

# Додавання обробника для виводу в консоль
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler()
# console_handler.setLevel(logging.DEBUG)
logging.getLogger('')

# Логування подій різного рівня
logging.debug('Message level DEBUG')
logging.info('Message level INFO')
logging.warning('Message level WARNING')
logging.error('Message level ERROR')
logging.critical('Message level CRITICAL')
