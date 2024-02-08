from user.models import Account
from ..handlers.DBHandler import AccountHandler
from ..handlers.EmailHandler import EmailHandler

class RegisterAction:
    def __init__(self,request):
        self.request = request

    def validate_registration_data(self):
        if not self.email or not self.password:
            return False,"email or password must be provided"
        # check email already exists or not
        account = Account.objects.filter(email=self.email)
        if(account.exists() and account.first().is_active):
            return False,"Email already exists"
        return  True,None
        
    def prepare_registration_data(self):
        self.email = self.request.data.get('email')
        self.password = self.request.data.get('password')

        return self.validate_registration_data()
    
    def perform_registration_action(self):
        account_handler = AccountHandler(self.email,self.password)
        try:
            if account_handler.check_unverified_account_already_present():
                return False,"Verification email already sent to the given email. Please verify it!"
            account_handler.create_unverified_account()
            print("Unverif")
            email_handler = EmailHandler(request=self.request,email=self.email,account=account_handler.account)
            if not email_handler.send_registration_verification_email():
                return False,"Verification Email was not sent"
            print("Email Sent!")
            return True,"Registration Successful!"
        except Exception as err:
            return False,str(err)

    def execute(self):
        status,response = self.prepare_registration_data()
        if status:
            return self.perform_registration_action()
        return False,response