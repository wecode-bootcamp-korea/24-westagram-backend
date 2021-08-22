from django.shortcuts import render

# Create your views here.

import json
from django.http  import JsonResponse
from django.views import View
from users.models import User

class UserView(View):
    def post(self,request):
        try:
            data       = json.loads(request.body)
            user = User.objects.create(
                    first_name = data['first_name'],
                    last_name  = data['last_name'],
                    email      = data['email'],
                    password   = data['password'],
                    phone_number = data['phone_number'],
                    gender     = data['gender']
                    birth      = data['birthday']
                    )
            return JsonResponse(
                    {'message' : 'CREATED'}, 
                    status = 201
                    )
        except KeyError:
            return JsonResponse(
                    {'message' : 'KEY_ERROR'}, 
                    status = 400
                    )

