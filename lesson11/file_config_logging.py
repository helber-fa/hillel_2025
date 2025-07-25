import logging
import logging.config

import pathlib
import os
file_path = os.path.join(str(pathlib.Path(__file__).parent.parent), "logging_config.ini")
logging.config.fileConfig(file_path)

# Використання логера
logger = logging.getLogger('sampleLogger')
my_custom_logger = logging.getLogger("myCustomLogger")

logger.debug('Message level DEBUG')
logger.info('Message level INFO')
my_custom_logger.error("ERROR!! ERROR!!! something goes wrong")
