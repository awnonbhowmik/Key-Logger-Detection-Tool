# config.py

# Directories to monitor for suspicious file activity
DIRECTORIES_TO_MONITOR = ["/path/to/monitor"]

# Trusted IP addresses
TRUSTED_IPS = ['192.168.1.1', '127.0.0.1']

# Email alert settings
EMAIL_SETTINGS = {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "from_email": "your_email@example.com",
    "password": "your_password",
    "to_email": "admin@example.com"
}

# Twilio SMS alert settings
TWILIO_SETTINGS = {
    "account_sid": "your_account_sid",
    "auth_token": "your_auth_token",
    "from_number": "your_twilio_number",
    "to_number": "+1234567890"
}
