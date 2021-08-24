import json
import re
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from .models import User
from my_settings import MY_SECRET_KEY


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message": "EMAIL Already Exist"}, status=400)

            email_validator = re.compile(
                "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            )
            password_validator = re.compile(
                "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
            )
            is_email_valid    = email_validator.match(data["email"])
            is_password_valid = password_validator.match(data["password"])

            if not (is_email_valid and is_password_valid):
                return JsonResponse({"message": "INVALID INPUT FORMAT"}, status=400)

            User.objects.create(
                name          = data["name"],
                email         = data["email"],
                password      = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                phone_number  = data["phone_number"],
                date_of_birth = data["date_of_birth"],
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            user = User.objects.get(email=data["email"])
            
            if not bcrypt.checkpw(data["password"].encode("utf-8"), user.password.encode("utf-8")):
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            token = jwt.encode({"user": user.id}, MY_SECRET_KEY, algorithm="HS256")
            return JsonResponse({"message": "SUCCESS", "token": token}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
