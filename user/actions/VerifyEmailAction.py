from user.models import Account
from user.handlers.DBHandler import AccountHandler


class VerifyEmailAction:
    def __init__(self,request):
        self.request = request

    def validate_email_data(self):
        if not self.request.GET.get('email') or not self.request.GET.get('token'):
            return False,"Email and token are required to verify"
        else:
            return True,""

    def prepare_email_data(self):
        self.email = self.request.GET.get('email')
        self.token = self.request.GET.get('token')
        return self.validate_email_data()
    
    def perform_verify_email(self):
        account = Account.objects.filter(email=self.email,token=self.token)
        if not account.exists():
            return False,"Invalid email or token"
        AccountHandler.verify_account(account.first())
        return True,"Account verified successfully!"

        
    def execute(self):
        status,message = self.prepare_email_data()
        if not status:
            return False,message
        return self.perform_verify_email()
        

