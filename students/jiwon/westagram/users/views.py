import json, re 

from django.http     import JsonResponse
from django.views    import View

from users.models import User


class SignupView(View):
    def post(self, request):
        data                = json.loads(request.body)
        email_validation    = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")  
            
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'MESSAGE':"ALREADY EXISTED EMAIL"}, status=400)

        if not email_validation.match(data['email']):
            return JsonResponse({"MESSAGE":"EMAIL_ERROR"}, status=400)

        if not password_validation.match(data['password']):
            return JsonResponse({"MESSAGE":"PASSWORD_ERROR"}, status=400)

        User.objects.create(
            name            = data['name'],
            email           = data['email'],
            password        = data['password'],
            phone_number    = data['phone_number'],
            favorite_food   = data['favorite_food']
            )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists(): 
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            if User.objects.get(email = data['email']).password == data['password']:
                return JsonResponse({"message": "SUCCESS"}, status=200)
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)