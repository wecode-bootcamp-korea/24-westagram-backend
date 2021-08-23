import re

from django.http import JsonResponse as JR

class EmailValidationError(Exception):
    def __init__(self):
        super().__init__('EmailValidationError')

class PasswordValidationError(Exception):
    def __init__(self):
        super().__init__('PasswordValidationError')

class AlreadyExist(Exception):
    def __init__(self):
        super().__init__('AlreadyExist')

def Raise_validation(email, password):
    if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise EmailValidationError
    
    if not re.match('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', password):
        raise PasswordValidationError
    return

