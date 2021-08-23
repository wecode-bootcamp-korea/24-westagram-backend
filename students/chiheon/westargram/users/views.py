# Create your views here.

import json

from django.http  import JsonResponse
from django.views import View

from users.models import User
from . validation import EmailValidation, PasswordValidation

class UserView(View):
    def post(self,request):
        data          = json.loads(request.body)
        email_data    = data['email']
        password_data = data['password']

        try:
            if User.objects.filter(email = email_data).exists():
                return JsonResponse({'MESSAGE' : 'EMAIL ALREADY EXISTS'}, status = 400)
            
            if EmailValidation(email_data):
                return JsonResponse({'MESSAGE' : 'EMAIL VALIDATION ERROR'}, status = 400)

            if PasswordValidation(password_data):
                return JsonResponse({'MESSAGE' : 'PASSWORD VALIDATION ERROR'}, status = 400)
                
            user = User.objects.create(
                    first_name   = data['first_name'],
                    last_name    = data['last_name'],
                    email        = data['email'],
                    password     = data['password'],
                    phone_number = data['phone_number'],
                    gender       = data['gender'],
                    birth        = data['birth']
                    )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)
        
        except KeyError as k:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)