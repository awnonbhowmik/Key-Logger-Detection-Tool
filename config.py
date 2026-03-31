import os
from dotenv import load_dotenv

load_dotenv()

# Directories to monitor for suspicious file activity (colon-separated in env)
_dirs = os.environ.get("MONITOR_DIRECTORIES", "/tmp")
DIRECTORIES_TO_MONITOR = [d.strip() for d in _dirs.split(":") if d.strip()]

# Trusted IP addresses (comma-separated in env)
_ips = os.environ.get("TRUSTED_IPS", "127.0.0.1,192.168.1.1")
TRUSTED_IPS = [ip.strip() for ip in _ips.split(",") if ip.strip()]

# Email alert settings
EMAIL_SETTINGS = {
    "smtp_server": os.environ.get("SMTP_SERVER", "smtp.example.com"),
    "port": int(os.environ.get("SMTP_PORT", "587")),
    "from_email": os.environ.get("FROM_EMAIL", ""),
    "password": os.environ.get("EMAIL_PASSWORD", ""),
    "to_email": os.environ.get("TO_EMAIL", ""),
}

# Twilio SMS alert settings
TWILIO_SETTINGS = {
    "account_sid": os.environ.get("TWILIO_ACCOUNT_SID", ""),
    "auth_token": os.environ.get("TWILIO_AUTH_TOKEN", ""),
    "from_number": os.environ.get("TWILIO_FROM_NUMBER", ""),
    "to_number": os.environ.get("TWILIO_TO_NUMBER", ""),
}
