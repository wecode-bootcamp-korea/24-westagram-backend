import json
import re

from django.http  import JsonResponse
from django.views import View

from .models      import User

class SinupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            address      = data['address']

            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({'MESSAGE': "NOT_EMAIL"}, status=400)

            if not re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,2048}$", password):
                return JsonResponse({'MESSAGE': "INVALID_PASSWORD"}, status=400)
        
            if not re.match('^\d{3}-\d{3,4}-\d{4}$', phone_number):
                return JsonResponse({'MESSAGE': 'INVALID_PHONENUMBER'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE': 'REGISTERED_EMAIL'})

            user = User(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                address      = address
            )
            user.save()

            return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)
        except ValueError:
            return JsonResponse({'MESSAGE': "VALUE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE': "KEY_ERROR"}, status=400)
       

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            
            if not User.objects.filter(email=email).exists():
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status=401)

            user = User.objects.get(email=email)
            
            if user.password != password:
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status=401)

            return JsonResponse({"message": "SUCCESS"}, status=200)
        except ValueError:
            return JsonResponse({'MESSAGE': "VALUE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE': "KEY_ERROR"}, status=400)
