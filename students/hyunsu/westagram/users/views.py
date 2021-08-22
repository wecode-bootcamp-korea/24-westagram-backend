import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        emali_format = re.compile('\w+[@]\w+[.]\w+')
        password_compare = re.compile('^(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=])[0-9a-zA-Z!@#$%^&*]{8,}$')
       
        email_list = []

        users = User.objects.all()
        for user in users:
            email_list.append(user.email)

        if not (data['email'] and data['password']):
            return JsonResponse(
                {"message" : "KEY_ERROR"}, status=400)    
        
        if not emali_format.search(data['email']):
            return JsonResponse(
                {"message" : "Invalid Email Format"}, status=401)

        if (len(data['password']) < 8) or password_compare.match(data['password']):
            return JsonResponse(
                {"message" : "Invalid Password Format"}, status=402)

        if data['email'] in email_list:
            return JsonResponse(
                {"message":"Same Email Exist"}, status=403)
        
        user_info = User.objects.create(
            name         = data['name'],
            email        = data['email'],
            password     = data['password'],
            phone_number = data['phone_number'],
            address      = data['address']
        )

        return JsonResponse(
            {'message' : 'SUCCESS'}, status=201)
