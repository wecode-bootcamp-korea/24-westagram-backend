from datetime import datetime, timedelta
import json, bcrypt, jwt

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.db.utils import DataError

from users.models import  User
from . validation import email_validation, nickname_validation, password_validation
from my_settings import SECRET_KEY


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not email_validation(data['email']):
                return JsonResponse({'message': 'INVALID_EMIAL_FORMAT'}, status=400)
            if not nickname_validation(data['nickname']):
                return JsonResponse({'message': 'INVALID_NICKNAME_FORMAT'}, status=400)
            if not password_validation(data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD_FORMAT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'REGISTERED_USER'}, status=400)
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'message': 'REGISTERED_NICKNAME'}, status=400)

            salt = bcrypt.gensalt()
            encoded_password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, salt)
            decoded_password = hashed_password.decode('utf-8')

            User.objects.create(
                name     = data['name'],
                nickname = data['nickname'],
                email    = data['email'], 
                password = decoded_password,
                phone    = data['phone']
            )
            return JsonResponse({'message': 'SUCCESS!'}, status=201)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except DataError:
            return JsonResponse({'message': 'DATA_TOO_LONG'}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(email=data['email'])

        try:
            if User.objects.filter(email=data['email']).exists():
                encoded_input_password   = data['password'].encode('utf-8')
                encoded_db_password      = (user.password).encode('utf-8')
                access_token_expire_date = datetime.utcnow() + timedelta(hours=3)
    
                if bcrypt.checkpw(encoded_input_password, encoded_db_password):
                    access_token = jwt.encode(
                        {
                            'email': user.email,
                            'exp'  : access_token_expire_date
                        }, 
                        SECRET_KEY, algorithm = 'HS256'
                    )
                    return JsonResponse(
                        {
                            'message'    : 'LOGIN_SUCCESS', 
                            'token'      : access_token, 
                            'expire date': access_token_expire_date.strftime('%Y/%m/%d %H:%M:%S')
                        }, status=200
                    )

                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'EXPIRED_TOKEN'}, status=401)
        