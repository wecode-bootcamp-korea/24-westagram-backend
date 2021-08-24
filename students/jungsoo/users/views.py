import json
import re
import bcrypt

from django.views import View
from django.http import JsonResponse

from users.models import User

class UserView(View):
    def post(self, request):
        data           = json.loads(request.body)
        email_regex    = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])(?=.*[!@#$%^*+=-]).{8,}$')

        try:
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number'] 
            address      = data['address']

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message" : "EXIST USER"}, status = 400)
            elif not email_regex.match(data['email']):
                return JsonResponse({"message" : "INVALID_EMAIL"}, status = 400)
            elif not password_regex.match(data['password']):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 400)
            
            User.objects.create(
                name         = data['name'],
                email        = data['email'], 
                password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()),
                phone_number = data['phone_number'], 
                address      = data['address'], 
            )
            return JsonResponse({"message" : "SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']

            if User.objects.filter(email = data['email']).exists():
                if User.objects.get(email = data['email']).password == data['password']:
                    return JsonResponse({"message" : "SUCCESS"}, status = 200)
                else:
                    return JsonResponse({"message" : "INVALID_USER"}, status = 401)
            else:
                return JsonResponse({"message" : "INVALID_USER"}, status = 401)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)




    
