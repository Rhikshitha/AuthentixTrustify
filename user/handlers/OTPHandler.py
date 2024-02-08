from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.oath import totp
from django_otp.util import random_hex
from twilio.rest import Client
from user.models import OTP
from sms import send_sms
import os
import time
from dotenv import load_dotenv
load_dotenv()

class OTPHandler:
    def __init__(self,mobile_number,user):
        self.mobile_number=mobile_number
        self.user = user

    def generate_otp(self):
        secret_key = b'12345678901234567890'
        now = int(time.time())
        otp_value=totp(key=secret_key, step=10, digits=6)
        print(otp_value)
        otp_entry, is_created = OTP.objects.update_or_create(user=self.user, defaults={'otp_value': otp_value})
        return otp_value

    def send_otp_sms(self):
        client = Client(os.getenv("TWILLIO_SID"), os.getenv("TWILLIO_AUTH_TOKEN"))
        otp_value = self.generate_otp()
        print("OTP Value",otp_value,os.getenv("TWILLIO_MOBILE_NUMBER"))

        # message = client.messages.create(
        #     to=self.mobile_number,
        #     from_=os.getenv("TWILLIO_MOBILE_NUMBER"),
        #     body=f"Your OTP is: {otp_value}"
        # )
        try:
            print("SEnding otp",os.getenv("TWILLIO_AUTH_TOKEN"))
            print('+91'+str(self.mobile_number))
            message = client.messages.create(
                body=f"Your OTP is: {otp_value}",
                from_='+16316462656',
                to='+91'+str(self.mobile_number)
                )
            return True
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def verify_otp(self,user,entered_otp):
        otp = OTP.objects.filter(user=self.user, otp_value=entered_otp)
        if not otp.exists():
            return False
        otp.delete()
        return True
    
