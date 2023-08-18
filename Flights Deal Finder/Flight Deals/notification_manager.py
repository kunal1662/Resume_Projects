from twilio.rest import Client
TWILIO_SID = "AC0eb94c240dd5c9dde8125b238ac9ca75"
TWILIO_AUTH_TOKEN = "06e494334a76b99a568709233cf9252b"
TWILIO_VIRTUAL_NUMBER = "+18156058351"
TWILIO_VERIFIED_NUMBER = "+919729220008"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)