import os
import shutil
import re

class Config:

    def configure_user():
        user = input("\n-> Username: ")
        email = input("-> E-mail: ")
        
        def emailValidate(email):
            email_format = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            return re.match(email_format, email) is not None
        
        if emailValidate(email):
            with open(".gitto/config.ini", "w") as config:
                config.write(f"name = {user}\nemail = {email}")
            print("\n")
        else:
            print("-> Invalid email.\n")
