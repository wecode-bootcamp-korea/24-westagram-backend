from django.shortcuts import render

# Create your views here.

import json
from django.http  import JsonResponse
from django.views import View
from users.models import User
from . validation import *

class UserView(View):
    def post(self,request):
        data          = json.loads(request.body)
        email_data    = data['email']
        password_data = data['password']
        user_infos    = User.objects.all()
        user_emails   = []
        for user in user_infos:
            user_emails.append(user.email)
        try:
            if not '@' in email_data or Validate_email(email_data)=='ValidationError' or Validate_password(password_data)=='ValidationError':
                return JsonResponse(
                        {'message' : 'ValidationError'},
                        status = 400
                        )
            elif Validate_email(email_data)=='KeyError' or Validate_password(password_data)=='KeyError':
                return JsonResponse(
                        {'message' : 'KeyError'},
                        status = 400
                        )
            elif email_data in user_emails:
                return JsonResponse(
                        {'message' : 'AlreadyExists'},
                        status = 400
                        )
            user = User.objects.create(
                    first_name = data['first_name'],
                    last_name  = data['last_name'],
                    email      = data['email'],
                    password   = data['password'],
                    phone_number = data['phone_number'],
                    gender     = data['gender'],
                    birth      = data['birth']
                    )
            return JsonResponse(
                    {'message' : 'SUCCESS'}, 
                    status = 201
                    )
        except Exception as e:
            return JsonResponse(
                    {'message' : f'{e}'},
                    status = 400
                    )

