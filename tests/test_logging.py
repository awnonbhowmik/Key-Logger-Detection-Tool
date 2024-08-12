import unittest
import os
from logging.logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.log_file = "keylogger_detection.log"
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_alert(self):
        self.logger.log_alert("Test Alert")
        with open(self.log_file, "r") as f:
            logs = f.read()
            self.assertIn("Test Alert", logs)

    def test_log_event(self):
        self.logger.log_event("Test Event")
        with open(self.log_file, "r") as f:
            logs = f.read()
            self.assertIn("Test Event", logs)

if __name__ == "__main__":
    unittest.main()
