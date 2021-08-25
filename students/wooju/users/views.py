import json, re
import bcrypt, jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from my_settings import SECRET_KEY

class UsersView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            Valid_email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not Valid_email.match(email):
                return JsonResponse({'MESSAGE':'EMAIL_VALIDATION'}, status=400)
            
            Valid_password = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
            if not Valid_password.match(password):
                return JsonResponse({'MESSAGE':'PASSWORD_VALIDATION'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'AlREADY_EXISTED_EMAIL'}, status=400)
            
            salt             = bcrypt.gensalt()
            encoded_password = password.encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, salt)
            decoded_password = hashed_password.decode('utf-8')

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = decoded_password,
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

            if User.objects.filter(email=data['email']).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(email=data['email']).password.encode('utf-8')):
                    token = jwt.encode({'id' : User.objects.get(email=data['email']).id},SECRET_KEY, algorithm='HS256')
                    return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN' : token}, status=200)
            
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
            
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)