import json
import re
import bcrypt

from django.http import JsonResponse
from django.views import View

from users.models import User

class UsersView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            email               = data["email"]
            password            = data["password"]
            email_validation    = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
            password_validation = re.compile("^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$")
            
            if not email_validation.match(email):
                return JsonResponse({"message":"EMAIL_VALIDATION_ERROR"}, status=400)

            if not password_validation.match(password):
                return JsonResponse({"message":"PASSWORD_VALIDATION_ERROR"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message":"DUPLICATION_ERROR"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_hashed_password = hashed_password.decode('utf-8')

            User.objects.create(
                name           = data["name"],
                email          = data["email"],
                password       = decoded_hashed_password,
                contact_mobile = data["contact_mobile"],
                nickname       = data["nickname"],
                address        = data["address"],
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)


class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if not User.objects.filter(email=data['email'], password=data['password']).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)
            
            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)