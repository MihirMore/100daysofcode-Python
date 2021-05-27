from twilio.rest import Client
import smtplib

TWILIO_SID = "Your APP S_ID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR NUMBER"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "yOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP_SSL(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
