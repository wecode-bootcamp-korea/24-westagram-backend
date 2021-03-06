import re
import json
import bcrypt
import jwt
from json.decoder import JSONDecodeError

from my_settings import SECRET_KEY, ALGORITHM
from django.http import JsonResponse
from django.views import View

from .models import User


class SignUp(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data["name"]
            email        = data["email"]
            password     = data["password"]
            phone_number = data["phone_number"]

            
            email_regex    = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
            password_regex = re.compile("^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$")

            if not email_regex.match(email):
                return JsonResponse({"message": "E-MAIL_VALIDATION_ERROR"}, status=400)

            elif not password_regex.match(password):
                return JsonResponse({"message": "PASSWORD_VALIDATION_ERROR"}, status=400)

            elif User.objects.filter(email=email).exists():
                return JsonResponse({"message": "USER_ALREADY_EXIST"}, status=400)

            else:
                user = User.objects.create(
                    name         = name,
                    email        = email,
                    password     = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                    phone_number = phone_number,
                    bio          = data.get("bio"),
                )

                created_user = {
                    "name": user.name,
                    "email": user.email,
                    "phone_number": user.phone_number,
                    "bio": user.bio,
                }

                return JsonResponse(
                    {"Message": "SUCCESS", "Result": created_user}, status=201
                )
        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class Login(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email    = data["email"]
            password = data["password"]

            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)

                if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
                    encoded_jwt = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm=ALGORITHM)
                    return JsonResponse({"access_token": encoded_jwt, "user_id": user.id}, status=200)

                return JsonResponse({"message": "INVALID_USER : Password"}, status=401)
            
            return JsonResponse({"message": "INVALID_USER : E-mail"}, status=401)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)