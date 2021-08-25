import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from my_settings import SECRET_KEY


class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

            encoded_jwt = jwt.encode({'user-id':user.id}, SECRET_KEY, algorithm='HS256')
            JsonResponse({'MESSAGE':'SUCCESS', 'token':encoded_jwt}, status=200)
            
            return response
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not re.compile('^[a-zA-Z0-9!#$%^&*()]+@[a-z]+.[a-z]+$').match(data['email']):
                return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'},status=400)

            if not re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,100}$').match(data['password']):
                return JsonResponse({'MESSAGE':'INVALID_PASSWORD_ERROR'},status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE':'DUPLICATION_ERROR'}, status=400)

            hashed_password = bcrypt.hashpw( data['password'].encode('utf-8'), bcrypt.gensalt() )

            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = hashed_password.decode(),
                phone    = data['phone']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)



