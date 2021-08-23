import json, re  #정규표현식 지원모듈 re
from django.shortcuts import render
# from users.apps import ProductsConfig 
from django.http     import JsonResponse
from django.views    import View
from users.models import User


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        email_validation    = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
        # password    = data['password']
        # email       = data['email']

        if data['password'] == '' or data['email'] == '':
            return JsonResponse({'message':"KEY_ERROR"}, status=400)    #이메일이나 패스워드가 전달되지 않을 경우
            
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'message':"email already exists"}, status=400)    #이메일이 중복될 때

        if email_validation.match(data['email']) == None:
            return JsonResponse({"MESSAGE":"INPUT_ERROR"}, status=400)   #이메일이나 패스워드가 규격에 맞지 않을 때

        if password_validation.match(data['password']) == None:
            return JsonResponse({"MESSAGE":"PASS_ERROR"}, status=400)

        User.objects.create(
            name            = data['name'],
            email           = data['email'],
            password        = data['password'],
            phone_number    = data['phone_number'],
            favorite_food   = data['favorite_food']
            )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)