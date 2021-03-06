import json
import re
import bcrypt
import jwt

from my_settings  import SECRET_KEY
from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        data             = json.loads(request.body)
        emali_format     = re.compile('\w+[@]\w+[.]\w+')
        password_compare = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')

        try:   
            if not emali_format.search(data['email']):
                return JsonResponse({"message" : "INVALID EMAIL FORMAT"}, status=400)

            if password_compare.match(data['password']):
                return JsonResponse({"message" : "INVALID PASSWORD FORMAT"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "SAME EMAIL EXIST"}, status=400)
            
            salt             = bcrypt.gensalt()
            encode_password  = data['password'].encode('utf-8')
            hash_password    = bcrypt.hashpw(encode_password, salt)
            decode_password  = hash_password.decode('utf-8')
            
            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = decode_password,
                phone_number = data['phone_number'],
                address      = data['address']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
       
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class UserSign(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401)
            
            user = User.objects.get(email=data['email'])
            
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user_id.password.encode('utf-8')):
                return JsonResponse({"message" : "INVALID_USER"}, status=401)

            encode_jwt = jwt.encode({'user id' : user.id}, SECRET_KEY , algorithm='HS256')
        
            return JsonResponse({
                "message" : "SUCCESS",
                "token" : encode_jwt,
                }, status=200)

        except KeyError:
            return JsonResponse({'message' : "KEY_ERROR"}, status=400)