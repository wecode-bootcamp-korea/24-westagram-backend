import re

'''
class EmailValidationError(Exception):
    def __init__(self):
        super().__init__('EmailValidationError')

class PasswordValidationError(Exception):
    def __init__(self):
        super().__init__('PasswordValidationError')

class AlreadyExist(Exception):
    def __init__(self):
        super().__init__('AlreadyExist')
'''

def EmailValidation(email):
    if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    
    return False

def PasswordValidation(password):
    if not re.match('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', password):
        return True
    
    return False

