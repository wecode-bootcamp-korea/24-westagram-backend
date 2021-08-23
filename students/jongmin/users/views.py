import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from users.models import User

# Create your views here.
class UsersView(View):
    def post(self, request):
        data = json.loads(request.body)
        User.objects.create(
            name         = data['name'],
            phone_number = data['phone_number'],
            gender       = data['gender'],
            address      = data['address'],
            birth        = data['birth'],
            email        = data['email'], #정규표현신식으로
            password     = data['password']
        )
