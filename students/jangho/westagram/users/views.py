from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
import json

from validation import email_validation, nickname_validation, pw_validation
from users.models import User

class SignUpView(View):
    def post(self, request):

        def create_user():
            User.objects.create(
                name     = data['name'],
                nickname = data['nickname'],
                email    = data['email'], 
                password = data['password'],
                phone    = data['phone']
            )
        
        data = json.loads(request.body)
        try:
            nickname_validation(data)
            email_validation(data)
            pw_validation(data)

            if User.objects.filter(name=data['nickname']).exists():
                return JsonResponse({'message': 'REGISTERED_NICKNAME'})
            if User.objects.filter(name=data['email']).exists():
                return JsonResponse({'message': 'REGISTERED_USER'})
            else:
                create_user()
                return JsonResponse({'message': 'SUCCESS!'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except Exception as ex:
            return JsonResponse({'message':'Error!!'}, ex)
