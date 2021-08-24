import json
import re
import bcrypt

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from users.models import User

class SignUpView(View):
    
    def post(self,request):
        data = json.loads(request.body)
        
        try:
            check_password = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
            password_validator = check_password.match(data['password'])

            if not password_validator:
                return JsonResponse({"MESSAGE" : "PASSWORD FORM ERROR"}, status=404)
            
            if len(User.objects.filter(email=data["email"])) > 0:
                return JsonResponse({"MESSAGE" : "EMAIL DUPLICATION ERROR"}, status=404)
                
            check_email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            email_validator = check_email.match(data["email"])

            if not email_validator:
                return JsonResponse({"MESSAGE" : "EMAIL FORM ERROR"}, status=404)

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

class SignInView(View):
        
    def post (self,request):
        data = json.loads(request.body)
        
        try:
            user_check = User.objects.filter(email=data["email"])
            
            if not user_check.exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)
            
            if not user_check.filter(password=data["password"]).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)

            return  JsonResponse({"MESSAGE": "SUCCESS"}, status=200)

        except KeyError as e:
            return  JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)