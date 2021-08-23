import json
import re

from django.http import JsonResponse
from django.views import View

from .models import User


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message": "EMAIL Already Exist"}, status=400)
            else:
                email_validator = re.compile(
                    "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                )
                password_validator = re.compile(
                    "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
                )
                is_email_valid = email_validator.match(data["email"])
                is_password_valid = password_validator.match(data["password"])

                if not (is_email_valid and is_password_valid):
                    return JsonResponse({"message": "INVALID INPUT FORMAT"}, status=400)

            User.objects.create(
                name=data["name"],
                email=data["email"],
                password=data["password"],
                phone_number=data["phone_number"],
                date_of_birth=data["date_of_birth"],
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
