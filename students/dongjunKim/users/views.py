import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

import re

class SignupView(View) :
    def post(self, request) :
        data = json.loads(request.body)
        if ('email' not in data) or ('password' not in data): 
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        email_checker = re.compile('^[a-zA-Z0-9!#$%^&*()]+@[a-z]+.[a-z]+$')
        valid_email = email_checker.match(data['email'])
        if not valid_email :
            return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'},status=400)
        password_checker = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,100}$')
        valid_password = password_checker.match(data['password'])
        if not valid_password :
            return JsonResponse({'MESSAGE':'INVALID_PASSWORD_ERROR'},status=400)
        try :
            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except IntegrityError as e:
            return JsonResponse({'MESSAGE':'DUPLICATION_ERROR'}, status=400)

class LoginView(View) :
    def post(self, request) :
        data = json.loads(request.body)
        if ('email' not in data) or ('password' not in data): 
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        try :
            user = User.objects.get(email=data['email'])
            if user.password != data['password'] :
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
        except User.DoesNotExist as e :
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)





