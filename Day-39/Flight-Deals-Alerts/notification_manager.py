from twilio.rest import Client

TWILIO_SID = "AC446baf82e5cca3dbae630af5116cd96a"
TWILIO_AUTH_TOKEN = "60d9a074e92fe3013e3eb36fa1561bf5"
TWILIO_VIRTUAL_NUMBER = "+16503977270"
TWILIO_VERIFIED_NUMBER = "+91 90824 90234"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        print(f"Send sms called for {message}")
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)
