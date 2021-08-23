import json
import re

from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View

from django.db.models.fields import EmailField

from users.models     import User

class UsersView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name              = data['name']
            email             = data['email']
            password          = data['password']
            cell_phone_number = data['cell_phone_number']

            # Email Validation
            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({'MESSAGE':'Wrong e-mail form'}, status=400)

            # Password Validation
            if not re.match('^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,}$', password):
                return JsonResponse({'MESSAGE':'Wrong password form'}, status=400)

            # Cell Phone Validation
            if not re.match('^\d{3}-\d{3,4}-\d{4}$', cell_phone_number):
                return JsonResponse({'MESSAGE':'Wrong cell phone number form'}, status=400)

            # Duplication Email Validation
            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'Existed e-mail'}, status=400)

            user = User.objects.create(
                name = name,
                email = email,
                password = password,
                cell_phone_number = cell_phone_number
            )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)



        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)