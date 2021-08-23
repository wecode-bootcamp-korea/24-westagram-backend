import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User


class SignupView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            if not re.compile('^[a-zA-Z0-9!#$%^&*()]+@[a-z]+.[a-z]+$').match(data['email']) :
                return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'},status=400)
            
            if not re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,100}$').match(data['password']) :
                return JsonResponse({'MESSAGE':'INVALID_PASSWORD_ERROR'},status=400)
            
            if User.objects.filter(email=email).exists() :
                return JsonResponse({'MESSAGE':'DUPLICATION_ERROR'}, status=400)
            
            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone']
            )
            
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        
        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
