import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class UsersView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            Valid_email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$') # + = 1개 이상이 무조건 와야한다
            if not Valid_email.match(email):
                return JsonResponse({'MESSAGE':'EMAIL_VALIDATION'}, status=400)
            
            Valid_password = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$') # * = 0개 이상 무족와야한다
            if not Valid_password.match(password):
                return JsonResponse({'MESSAGE':'PASSWORD_VALIDATION'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'AlREADY_EXISTED_EMAIL'}, status=400)
            
            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = data['password'],
                phone_number  = data['phone_number'],
                date_of_birth = data['date_of_birth'],
            )

            return JsonResponse({'MESSAGE':'CREATE'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

class LoginsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if not User.objects.filter(email=data['email'],password=data['password']).exists():
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
            
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
            
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)