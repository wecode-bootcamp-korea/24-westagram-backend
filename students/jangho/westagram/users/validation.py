import re

from django.http import JsonResponse, HttpResponse


def email_validation(email_input) -> bool:
    if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_input):
        return False
    else:
        return True

def nickname_validation(nickname_input) -> bool:
    if not re.match('[A-Za-z0-9ㄱ-ㅎ가-힣]', nickname_input):
        return False
    else:
        return True

def password_validation(password_input) -> bool:
    if not re.match('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*^#?&])[A-Za-z\d$@$!%*^#?&]{8,}$', password_input):
        return False
    else:
        return True