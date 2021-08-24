import json
import re 

from django.http import JsonResponse
from django.views import View

from users.models import User

# Create your views here.
class Signup(View):
    def post(self, request):        
        try: 
            data = json.loads(request.body)
            
            name          = data['name']
            phone_number  = data['phone_number']
            gender        = data['gender']
            address       = data['address']
            birth         = data['birth']
            email         = data['email']
            password      = data['password']

            if not re.match('^\d{3}-\d{3,4}-\d{4}$', phone_number):
                return JsonResponse({"MESSAGE": "INVALID_FORMAT"}, status =400)

            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({"MESSAGE": "INVALID_FORMAT"}, status =400)

            if not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*~])[A-Za-z\d~!@#$%^&*]{8,}', password):
                return JsonResponse({"MESSAGE":"INVALID_FORMAT"}, status =400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE":"AlREADY_EMAIL"})

            User.objects.create(
                name          = data['name'],
                phone_number  = data['phone_number'],
                gender        = data['gender'],
                address       = data['address'],
                birth         = data['birth'],
                email         = data['email'],
                password      = data['password']
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201) 
          
        except KeyError:
            JsonResponse({"MESSAGE":"KEY_ERROR"}, status =400)
            