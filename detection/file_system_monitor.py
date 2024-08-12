from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from logging.logger import Logger
import config

class KeyloggerFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.log'):  # Keyloggers often use .log files
            logger = Logger()
            logger.log_alert(f"Suspicious file created: {event.src_path}")

def monitor_file_system():
    logger = Logger()
    event_handler = KeyloggerFileHandler()
    observer = Observer()
    for directory in config.DIRECTORIES_TO_MONITOR:
        observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
