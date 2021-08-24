# Create your views here.

import json, bcrypt

from django.http  import JsonResponse
from django.views import View

from users.models import User
from . validation import EmailValidation, PasswordValidation

class UserView(View):
    def post(self, request):
        data                = json.loads(request.body)
        email_data          = data['email']
        password_data       = data['password']

        try:
            if User.objects.filter(email = email_data).exists():
                return JsonResponse({'MESSAGE' : 'EMAIL ALREADY EXISTS'}, status = 400)
            
            if EmailValidation(email_data):
                return JsonResponse({'MESSAGE' : 'EMAIL VALIDATION ERROR'}, status = 400)

            if PasswordValidation(password_data):
                return JsonResponse({'MESSAGE' : 'PASSWORD VALIDATION ERROR'}, status = 400)
            
            mySalt              = bcrypt.gensalt()
            encoded_password    = password_data.encode('utf-8')
            hashed_password     = bcrypt.hashpw(encoded_password, mySalt)
            decoded_password    = hashed_password.decode('utf-8')
            
            User.objects.create(
                    first_name   = data['first_name'],
                    last_name    = data['last_name'],
                    email        = data['email'],
                    password     = decoded_password,
                    phone_number = data['phone_number'],
                    gender       = data['gender'],
                    birth        = data['birth']
                    )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 201)
        
        except KeyError as k:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

class Login(View):
    def post(self, request):
        data          = json.loads(request.body)

        try:
            email_data    = data['email']
            password_data = data['password']

            if not User.objects.filter(email = email_data).exists():
                return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status = 401)

            elif User.objects.get(email = email_data).password != password_data:
                return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status = 401)
            
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

