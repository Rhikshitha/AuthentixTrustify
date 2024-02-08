from user.models import Account

class AccountHandler:
    def __init__(self,email,password):
        self.email=email
        self.password = password
    
    def check_unverified_account_already_present(self):
        try:
            account = Account.objects.filter(email=self.email,is_active=False)
            if Account.objects.filter(email=self.email).exists():
                self.account=account.first()
                return True
            else:
                print("CHeck NO account peresent")
                return False
        except:
            return False

    def create_unverified_account(self):
        try:
            print("Inside account creation")
            account = Account.objects.create_user(username=self.email,password=self.password,email=self.email)
            account.set_password(self.password)
            account.save()
            self.account=account
        except:
            raise "Error while creating the account"

    @staticmethod
    def verify_account(account):
        try:
            account.is_active = True
            account.save()
        except:
            raise "account is not present"



    
