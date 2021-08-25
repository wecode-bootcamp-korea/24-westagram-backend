import json
import bcrypt
import jwt
import re

from django.views import View
from django.http import JsonResponse

from users.models import User
from westagram.settings import SECRET_KEY

class SignUpView(View):
    
    def post(self,request):
        data = json.loads(request.body)
        
        try:
            check_password     = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
            password_validator = check_password.match(data['password'])

            if not password_validator:
                return JsonResponse({"MESSAGE" : "PASSWORD FORM ERROR"}, status=404)
            
            if len(User.objects.filter(email=data["email"])) > 0:
                return JsonResponse({"MESSAGE" : "EMAIL DUPLICATION ERROR"}, status=404)
                
            check_email     = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            email_validator = check_email.match(data["email"])

            if not email_validator:
                return JsonResponse({"MESSAGE" : "EMAIL FORM ERROR"}, status=404)

            origin_password  = data['password']
            hashed_password  = bcrypt.hashpw(origin_password.encode('utf-8'), bcrypt.gensalt())
            decoded_hash_pwd = hashed_password.decode('utf-8')  

            User.objects.create(
            name        = data["name"],
            email       = data["email"],
            password    = decoded_hash_pwd,
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
            if not User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)
            
            entered_pwd       = data['password']
            encoded_enter_pwd = entered_pwd.encode('utf-8')

            user_pwd         = User.objects.get(email=data["email"]).password
            encoded_user_pwd = user_pwd.encode('utf-8')

            user_id = User.objects.get(email=data["email"]).id           

            if bcrypt.checkpw(encoded_enter_pwd,encoded_user_pwd):

                access_token = jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm='HS256')

                return  JsonResponse({"MESSAGE": "SUCCESS", "TOKEN" : access_token}, status=200)
            else:    
                return  JsonResponse({"MESSAGE": "LOGIN_FAIL"}, status=400)
                


        except KeyError as e:
            return  JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
        