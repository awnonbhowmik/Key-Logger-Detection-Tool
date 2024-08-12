import psutil
from logging.logger import Logger

def detect_suspicious_processes():
    logger = Logger()
    suspicious_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['name'] in ['keylogger.exe', 'kl.exe']:  # Example process names
                suspicious_processes.append(proc.info)
                logger.log_alert(f"Suspicious process detected: {proc.info}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return suspicious_processes
