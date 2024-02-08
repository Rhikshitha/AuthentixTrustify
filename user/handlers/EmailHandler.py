from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.urls import reverse


class EmailHandler:
    def __init__(self,request,email,account):
        self.email = email
        self.request = request
        self.account = account
    
    def send_registration_verification_email(self):
        verification_token = get_random_string(length=32)
        verification_url = self.request.build_absolute_uri(reverse('verify_email')) + f'?token={verification_token}&email={self.email}'
        self.account.token = verification_token
        self.account.save()
        print(self.account)
        try:
            send_mail(
                    'Verify your email',
                    f'You have successfully created an account in authentixtrustify. Click this link to verify your email: {verification_url}\n\nRegards,\nauthentixtrustify',
                    settings.EMAIL_HOST_USER,
                    [self.email],
                    fail_silently=False,
            )
            return True
        except Exception as e:
            print(e)
            return False

