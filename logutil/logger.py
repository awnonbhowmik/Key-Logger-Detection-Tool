import logging
import os

_LOG_FILE = os.environ.get("LOG_FILE", "keylogger_detection.log")

# Module-level named logger — avoids root logger pollution and
# ensures setup runs exactly once regardless of how many Logger instances are created.
_logger = logging.getLogger("keylogger_detection")

if not _logger.handlers:
    _logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(_LOG_FILE)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)


class Logger:
    def __init__(self):
        self._log = _logger

    def log_alert(self, message):
        self._log.warning(message)

    def log_event(self, message):
        self._log.info(message)

    def log_error(self, message):
        self._log.error(message)
