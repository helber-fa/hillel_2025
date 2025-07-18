import unittest
import logging

class TestLogging(unittest.TestCase):
    def test_log_warning(self):
        logger = logging.getLogger(__name__)
        with self.assertLogs(logger=logger, level='WARNING'):  # debug => info => warning => error => critical
            logger.info("This is a warning message")

if __name__ == '__main__':
    unittest.main()