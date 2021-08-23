import json, re

from django.http      import JsonResponse
from django.shortcuts import render
from django.views     import View
from .models           import User


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user_info = {
                'name'        : data["name"],
                'email'       : data["email"],
                'password'    : data["password"],
                'phone_number': data["phone_number"],
                'address'     : data["address"],
            }
            if not user_info['name'] or not user_info['email']:
                return JsonResponse({"message": "VALUE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)

        if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', user_info['email']):
            return JsonResponse({"message": "INVALID EMAIL FORMAT"}, status = 400)

        if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{12,40}", user_info['password']):
            return JsonResponse({"message": "INVALID_PASSWORD_FORMAT"}, status = 400)

        if User.objects.filter(email=user_info['email']).exists():
            return JsonResponse({"message": "THIS EMAIL ALREADY EXISTS"}, status = 400)

        User.objects.create(
            name        = user_info['name'],
            email       = user_info['email'],
            password    = user_info['password'],
            phone_number= user_info['phone_number'],
            address     = user_info['address']
        )

        return JsonResponse({"message": "SUCCESS"}, status = 201)


