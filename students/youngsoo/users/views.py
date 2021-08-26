import json
import re
import bcrypt
import jwt

from django.views import View
from django.http import JsonResponse

from users.models import User
from my_settings import SECRET_KEY

# Registering a user 
class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not re.search('[a-zA-Z0-9.+-]+@'
                                    '[a-zA-Z0-9-]+\.'
                                    '[a-zA-Z0-9.]+', data['email']) :
                return JsonResponse({'message' : 'INVALID EMAIL'}, status = 400)
            
            if not re.fullmatch('^(?=.*[a-z])(?=.*[A-Z])'
                                          '(?=.*\d)(?=.*[@$!%*?&])'
                                          '[A-Za-z\d@$!%*?&]{8,10}$', data['password']):
                return JsonResponse({'message' : 'INVALID PASSWORD'}, status = 400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'EMAIL DUPLICATE'}, status = 400)

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
                phone_number  = data['phone_number'],
                date_of_birth = data['date_of_birth'],
                gender        = data['gender'],
                address       = data['address'],
            )

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email=data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm='HS256')
                    return JsonResponse({'message' : 'SUCCESS', 'TOKEN' : token}, status = 200)
                
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
        