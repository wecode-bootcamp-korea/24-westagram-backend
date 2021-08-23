import re
import json
from json.decoder import JSONDecodeError

from django.http import JsonResponse
from django.views import View

from .models import User


class SignUp(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data.get("name")
            email        = data.get("email")
            password     = data.get("password")
            phone_number = data.get("phone_number")
            bio          = data.get("bio")

            if (not email) or (not password):
                return JsonResponse(
                    {"message": "KEY_ERROR"},
                    status=400,
                )

            else:
                email_regex = re.compile(
                    "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                )
                password_regex = re.compile(
                    "^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$"
                )

                if not email_regex.match(email):
                    return JsonResponse(
                        {"message": "E-MAIL_VALIDATION_ERROR"},
                        status=400,
                    )

                elif not password_regex.match(password):
                    return JsonResponse(
                        {"message": "PASSWORD_VALIDATION_ERROR"},
                        status=400,
                    )

                elif User.objects.filter(email=email).exists():
                    return JsonResponse(
                        {"message": "USER_ALREADY_EXIST"},
                        status=409,
                    )

                else:
                    user = User.objects.create(
                        name         = name,
                        email        = email,
                        password     = password,
                        phone_number = phone_number,
                        bio          = bio,
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