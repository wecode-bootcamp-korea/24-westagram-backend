import json
import re

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

            if email == "" or password == "":
                return JsonResponse({"message":"KEY_ERROR"}, status=400)
            
            if not email_validation.match(email):
                return JsonResponse({"message":"EMAIL_VALIDATION_ERROR"}, status=400)

            if not password_validation.match(password):
                return JsonResponse({"message":"PASSWORD_VALIDATION_ERROR"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message":"DUPLICATION_ERROR"}, status=400)

            User.objects.create(
                name           = data["name"],
                email          = data["email"],
                password       = data["password"],
                contact_mobile = data["contact_mobile"],
                nickname       = data["nickname"],
                address        = data["address"],
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)