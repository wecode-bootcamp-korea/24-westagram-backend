import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from django.db import IntegrityError
import re

class SignupView(View) :
    def post(self, request) :
        data = json.loads(request.body)
        if ('email' not in data) or ('password' not in data): #password, email 포함 확인
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        #Validation
        #1. email
        #- A@B.C 의 패턴만 유효하다. @과 .는 반드시 포함되어야 하며, A는 알파벳과 특수문자, B 와 C는 소문자 알파벳이 올 수 있다.
        email_checker = re.compile('^[a-zA-Z0-9!#$%^&*()]+@[a-z]+.[a-z]+$')
        valid_email = email_checker.match(data['email'])
        if not valid_email :
            return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'},status=400)
        #2. password
        # 8자이상 100자이하, 적어도 하나의 소문자,대문자,특수문자 포함
        password_checker = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,100}$')
        valid_password = password_checker.match(data['password'])
        if not valid_password :
            return JsonResponse({'MESSAGE':'INVALID_PASSWORD_ERROR'},status=400)
        #Email Duplication
        #유저 등록 시, 동일한 이메일의 데이터가 있는 경우 정합성 예외처리 
        try :
            #register user
            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
            #
        except IntegrityError as e:
            return JsonResponse({'MESSAGE':'DUPLICATION_ERROR'}, status=400)
