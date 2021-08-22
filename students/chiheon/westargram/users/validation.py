import re

def Validate_email(email):
    email_regex = re.compile('[^a-zA-Z0-9_]')
    email_id = email.split('@')[0]
    if email_regex.search(email_id):
        return 'ValidationError'
    elif len(email_id)==0:
        return 'KeyError'
    return 'Success'

def Validate_password(password):
    password_regex = re.compile('[^a-zA-Z0-9_]')
    if len(password)==0:
        return 'KeyError'
    elif password.isdigit() or len(password) < 8 or not password_regex.search(password):
        return 'ValidationError'
    return 'Success'
