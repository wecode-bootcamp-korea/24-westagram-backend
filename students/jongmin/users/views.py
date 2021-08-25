import json
import re 
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from my_settings import SECRET_KEY

# Create your views here.
class Signup(View):
    def post(self, request):        
        try: 
            data = json.loads(request.body)
            print(data)
            
            name          = data['name']
            phone_number  = data['phone_number']
            gender        = data['gender']
            address       = data['address']
            birth         = data['birth']
            email         = data['email']
            password      = data['password']

            if not re.match('^\d{3}-\d{3,4}-\d{4}$', phone_number):
                return JsonResponse({"MESSAGE": "INVALID_PHONENUMBER"}, status=400)

            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({"MESSAGE": "INVALID_EMAIL"}, status=400)

            if len(password) < 8:
                return JsonResponse({"MESSAGE":"INVALID_PASSWORD"}, status=400)
           
            if User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE":"AlREADY_EMAIL"})
            
            User.objects.create(
                name          = data['name'],
                phone_number  = data['phone_number'],
                gender        = data['gender'],
                address       = data['address'],
                birth         = data['birth'],
                email         = data['email'],
                password      = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201) 
          
        except KeyError:
            JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)
        except ValueError:
            JsonResponse({"MESSAGE":"Value_ERROR"}, status=400)

class Login(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            if not User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status=401)
            
            user = User.objects.get(email = email)
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                 return JsonResponse({"MESSAGE": "INVALID_PASSWORD"}, status=401)

            ticket = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256') 
            return JsonResponse({"MESSAGE":"SUCCESS", "TOKEN": ticket}, status=200)
               
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)