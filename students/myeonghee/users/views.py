from django.shortcuts import render

import json
from django.views import View

from django.http import JsonResponse
from users.models import User
import re

# Create your views here.
class SignUpView(View):
    
    def post(self,request):
        
        data = json.loads(request.body)
        
        try:
            if not data["email"] or not data["password"]:
                return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
            
            else:
                check_password = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
                password_validator = check_password.match(data['password'])

                if password_validator == None:
                    return JsonResponse({"MESSAGE" : "비밀번호 형식을 지켜주세요"}, status=404)
                
                if len(User.objects.filter(email=data["email"])) > 0:
                    return JsonResponse({"MESSAGE" : "중복된 이메일이 있습니다."}, status=404)
                    
                check_email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
                email_validator = check_email.match(data["email"])

                if email_validator == None:
                    return JsonResponse({"MESSAGE" : "Email 형식을 지켜주세요"}, status=404)

                else :
                    User.objects.create(
                    name        = data["name"],
                    email       = data["email"],
                    password    = data["password"],
                    cell_number = data["cell_number"],    
                    address     = data["address"],
                    birthday    = data["birthday"],
                    sex         = data["sex"]
                )  
                    return JsonResponse({"MESSAGE" : "CREATE"}, status=201)
        
        except KeyError as e:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
        

class LogIn(View):
        def get (self,request):

            data = json.loads(request.body)

            email=data["email"]
            data=["password"]

            return JsonResponse({"MESSAGE" : "CREATE"}, status=201)