import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename="keylogger_detection.log", level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    def log_alert(self, message):
        logging.warning(message)
        print(message)  # Optional: Print to console

    def log_event(self, message):
        logging.info(message)
        print(message)  # Optional: Print to console
