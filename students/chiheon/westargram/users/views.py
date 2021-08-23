# Create your views here.

import json

from django.http  import JsonResponse as JR
from django.views import View

from users.models import User
from . validation import (
        EmailValidationError, 
        PasswordValidationError,
        AlreadyExist, 
        Raise_validation
        )

class UserView(View):
    def post(self,request):
        data          = json.loads(request.body)
        email_data    = data['email']
        password_data = data['password']

        try:
            if User.objects.filter(email = email_data).exists():
                raise AlreadyExist
            
            Raise_validation(email_data, password_data)
                
            user = User.objects.create(
                    first_name = data['first_name'],
                    last_name  = data['last_name'],
                    email      = data['email'],
                    password   = data['password'],
                    phone_number = data['phone_number'],
                    gender     = data['gender'],
                    birth      = data['birth']
                    )
            return JR({'message' : 'SUCCESS'}, status = 201)
        
        except EmailValidationError as emailError:
            return JR({'message' : f'{emailError}'}, status = 403)
        
        except PasswordValidationError as pwdError:
            return JR({'message' : f'{pwdError}'}, status = 403)

        except AlreadyExist as a:
            return JR({'message' : f'{a}'}, status = 402)
        
        except KeyError as k:
            return JR({'message' : 'KEY_ERROR'}, status = 40)
