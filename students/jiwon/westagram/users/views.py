import json, re, bcrypt, jwt

from django.http     import JsonResponse
from django.views    import View

from users.models import User
from my_settings import SECRET_KEY 

class SignupView(View):
    def post(self, request):
        data                = json.loads(request.body)
        email_validation    = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")  
        password = data['password']
            
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'MESSAGE':"ALREADY EXISTED EMAIL"}, status=400)

        if not email_validation.match(data['email']):
            return JsonResponse({"MESSAGE":"EMAIL_ERROR"}, status=400)

        if not password_validation.match(data['password']):
            return JsonResponse({"MESSAGE":"PASSWORD_ERROR"}, status=400)

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        decoded_password = hashed_password.decode('utf-8')

        User.objects.create(
            name            = data['name'],
            email           = data['email'],
            password        = decoded_password,
            phone_number    = data['phone_number'],
            favorite_food   = data['favorite_food']
            )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if User.objects.filter(email=data['email']).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), (User.objects.get(email = data['email']).password).encode('utf-8')):
                    access_token = jwt.encode({"id": User.objects.get(email = data['email']).id }, SECRET_KEY , algorithm="HS256")
                    return JsonResponse({"message": "SUCCESS", 'token' : access_token}, status=200)
                return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)