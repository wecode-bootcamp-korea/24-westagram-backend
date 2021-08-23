import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        data             = json.loads(request.body)
        emali_format     = re.compile('\w+[@]\w+[.]\w+')
        password_compare = re.compile('^(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=])[0-9a-zA-Z!@#$%^&*]{8,}$')

        try:   
            if not emali_format.search(data['email']):
                return JsonResponse({"message" : "INVALID EMAIL FORMAT"}, status=400)

            if password_compare.match(data['password']):
                return JsonResponse({"message" : "INVALID PASSWORD FORMAT"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "SAME EMAIL EXIST"}, status=400)
            
            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
                address      = data['address']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
       
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
