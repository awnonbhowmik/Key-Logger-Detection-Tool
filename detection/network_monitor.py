import psutil
from logging.logger import Logger
import config

def monitor_network_activity():
    logger = Logger()
    suspicious_connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.raddr:
            remote_ip, remote_port = conn.raddr
            if remote_ip not in config.TRUSTED_IPS:
                suspicious_connections.append(conn)
                logger.log_alert(f"Suspicious network activity detected: {remote_ip}:{remote_port}")
    return suspicious_connections
