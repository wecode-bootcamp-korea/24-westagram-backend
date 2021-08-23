import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class LoginView(View) :
    def post(self, request) :        
        try :
            data = json.loads(request.body)
       
            if !User.objects.filter(email=data['email']).exists() :
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

            user = User.objects.get(email=data['email'])
        
            if user.password != data['password'] :
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
            
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
