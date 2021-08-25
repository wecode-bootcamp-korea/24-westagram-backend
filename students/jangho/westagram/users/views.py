import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from users.models import Comment, User
from . validation import email_validation, nickname_validation, password_validation

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
            User.objects.create(
                name     = data['name'],
                nickname = data['nickname'],
                email    = data['email'], 
                password = data['password'],
                phone    = data['phone']
            )
            return JsonResponse({'message': 'SUCCESS!'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)


class SignInView(View):
    def post(self, request):
        data        = json.loads(request.body)
        check_email = User.objects.filter(email=data['email'])

        try:
            if check_email.exists():
                user_data = User.objects.get(email=data['email'])
                print(user_data.email)
                if user_data.password == data['password']:
                    return JsonResponse({'message': 'LOGIN_SUCCESS'}, status=200)
                else:
                    return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            else:
                return JsonResponse({'message': 'INVALID_USER'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
    
