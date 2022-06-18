
import string
from tokenize import String
from filestore import save_data
# from send_mail import send_mail
import hashlib

# Initializaton of class
class Registration:
    def __init__(self) -> None:
        self.username=input('Enter your username: ') #input data in python
        self.email=input('Enter your email: ')
        self.full_name=input('Enter your full name: ')
        self.password= input('Enter the password: ')
        self.confirm_password=input('Confirm password: ')
    
    #Function to check whether two passwords match or not
    def check_password(self) -> str:  
        if self.password != self.confirm_password:
            raise Exception("password Mismatch")
        return self.password
    
    #Function for registration of the user
    def register(self):
        self.check_password() 
        self.generate_hash()
        # send_mail(self)
        save_data(self)
        print("Your are successfully registered as a user.")
    
    def generate_hash(self) -> str:
        plaintext = self.password.encode()
        d = hashlib.sha256(plaintext)
        self.hash = d.hexdigest()
        return self.hash




    
    # def send_mail(self):
    #     import smtplib

    #     sender = "admin@gmail.com"
    #     receiver = self.email
    #     print(receiver)

    #     message = f"""\
    #     Subject: Hi User
    #     To: {receiver}
    #     From: {sender}

    #     Thank You for your Registration."""

    #     with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    #         server.login("edc5057030e29c", "8fb5dfbf77df5a")
    #         print(server)
    #         try:
    #             server.sendmail(sender, receiver, message)
    #         except Exception as e:
    #             print(str (e))




