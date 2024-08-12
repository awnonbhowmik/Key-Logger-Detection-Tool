from twilio.rest import Client
import config

def send_sms_alert(message):
    client = Client(config.TWILIO_SETTINGS["account_sid"], config.TWILIO_SETTINGS["auth_token"])
    client.messages.create(
        body=message,
        from_=config.TWILIO_SETTINGS["from_number"],
        to=config.TWILIO_SETTINGS["to_number"]
    )
