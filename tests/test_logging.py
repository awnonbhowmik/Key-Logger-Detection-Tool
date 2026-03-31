import unittest
import logging
import io
from logutil.logger import Logger, _logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        # Capture log output in memory instead of relying on the file on disk.
        self._stream = io.StringIO()
        self._handler = logging.StreamHandler(self._stream)
        self._handler.setLevel(logging.DEBUG)
        _logger.addHandler(self._handler)

    def tearDown(self):
        _logger.removeHandler(self._handler)
        self._handler.close()

    def test_log_alert(self):
        Logger().log_alert("Test Alert")
        self._stream.seek(0)
        self.assertIn("Test Alert", self._stream.read())

    def test_log_event(self):
        Logger().log_event("Test Event")
        self._stream.seek(0)
        self.assertIn("Test Event", self._stream.read())


if __name__ == "__main__":
    unittest.main()
