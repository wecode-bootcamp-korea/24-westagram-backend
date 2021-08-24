import json
import re
import bcrypt

from django.http      import JsonResponse
from django.views     import View

from users.models     import User

# Sign Up View
class UsersView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            salt = bcrypt.gensalt()
            name              = data['name']
            email             = data['email']
            hashed_password   = bcrypt.hashpw(data['password'].encode('utf-8'), salt)
            cell_phone_number = data['cell_phone_number']

            # Email Validation
            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({'MESSAGE':'Wrong e-mail form'}, status=400)

            # Password Validation
            if not re.match('^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,}$', data['password']):
                return JsonResponse({'MESSAGE':'Wrong password form'}, status=400)

            # Cell Phone Validation
            if not re.match('^\d{3}-\d{3,4}-\d{4}$', cell_phone_number):
                return JsonResponse({'MESSAGE':'Wrong cell phone number form'}, status=400)

            # Duplication Email Validation
            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'Existed e-mail'}, status=400)

            User.objects.create(
                name              = name,
                email             = email,
                password          = hashed_password.decode('utf-8'),
                cell_phone_number = cell_phone_number
            )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)


# Log In View
class LoginsView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE':'INVALIDE USER'}, status=401)

            elif not User.objects.filter(password=data['password']).exists():
                return JsonResponse({'MESSAGE':'INVALIDE USER'}, status=401)
            
            return JsonResponse({'MESSSAGE':'LOG IN SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'MESSSAGE':'KEY_ERROR'}, status=400)


