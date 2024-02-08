from django.contrib.auth import login,authenticate

class LoginAction:
    def __init__(self,request):
        self.request = request
    
    def validate_login_data(self):
        if not self.email or not self.password:
            return False,"Email or Password is not given"
        return True,""
    
    def prepare_login_data(self):
        self.email = self.request.data.get("email")
        self.password = self.request.data.get("password")
        return self.validate_login_data()
    
    def perform_login(self):
        user = authenticate(username=self.email, password=self.password)
        if user is None:
            return False,"Invalid credentials"
        login(self.request,user)
        return True,"User logged in successfully"

    def execute(self):
        status,message = self.prepare_login_data()
        if not status:
            return False,message
        return self.perform_login()
        
    