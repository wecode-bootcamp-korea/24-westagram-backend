import json
import re

from django.views import View
from django.http import JsonResponse

from users.models import User

class SignupView(View):
    # Registering a user 
    def post(self, request):
        try:
            data = json.loads(request.body)

            email_valid = re.search('[a-zA-Z0-9.+-]+@'
                                    '[a-zA-Z0-9-]+\.'
                                    '[a-zA-Z0-9.]+', data['email'])      

            password_valid = re.fullmatch('^(?=.*[a-z])(?=.*[A-Z])'
                                          '(?=.*\d)(?=.*[@$!%*?&])'
                                          '[A-Za-z\d@$!%*?&]{8,32}$', data['password'])
            
            email_duplicate = User.objects.filter(email=data['email']).exists()

            if not email_valid:
                return JsonResponse({'message' : 'INVALID EMAIL'}, status = 400)
            
            if not password_valid:
                return JsonResponse({'message' : 'INVALID PASSWORD'}, status = 400)

            if email_duplicate:
                return JsonResponse({'message' : 'EMAIL DUPLICATE'}, status = 400)
            
            else:
                User.objects.create(
                    name          = data['name'],
                    email         = data['email'],
                    password      = data['password'],
                    phone_number  = data['phone_number'],
                    date_of_birth = data['date_of_birth'],
                    gender        = data['gender'],
                    address       = data['address'],
                )
                return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)


class LoginView(View):
    def get(self, request):
        data = json.loads(request.body)
        try:
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
            
            if not User.objects.filter(password=data['password']).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status = 401)

            else:
                return JsonResponse({'message' : 'SUCCESS'}, status = 200)
                
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

    

    
        



    
        

