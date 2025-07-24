import unittest
import logging
from test_functions import triangle_area

class LoggingTest(unittest.TestCase):
    def log_warning_test(self):
        logger = logging.getLogger(__name__)
        with self.assertLogs(logger=logger, level='WARNING'):  # debug => info => warning => error => critical
            logger.info("This is a warning message")

if __name__ == '__main__':
    unittest.main()