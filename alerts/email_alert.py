import smtplib
from email.mime.text import MIMEText
import config

def send_email_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config.EMAIL_SETTINGS["from_email"]
    msg["To"] = config.EMAIL_SETTINGS["to_email"]

    with smtplib.SMTP(config.EMAIL_SETTINGS["smtp_server"], config.EMAIL_SETTINGS["port"]) as server:
        server.starttls()
        server.login(config.EMAIL_SETTINGS["from_email"], config.EMAIL_SETTINGS["password"])
        server.sendmail(config.EMAIL_SETTINGS["from_email"], config.EMAIL_SETTINGS["to_email"], msg.as_string())
