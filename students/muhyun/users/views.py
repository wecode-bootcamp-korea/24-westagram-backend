import json, re, bcrypt

from django.http      import JsonResponse
from django.views     import View

from .models          import User


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not data['name'] or not data['email']:
                return JsonResponse({"message": "VALUE_ERROR"}, status=400)

            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']):
                return JsonResponse({"message": "INVALID EMAIL FORMAT"}, status=400)

            if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{12,40}",
                            data['password']):
                return JsonResponse({"message": "INVALID_PASSWORD_FORMAT"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "THIS EMAIL ALREADY EXISTS"}, status=400)

            password = data['password'].encode('utf-8')
            salt = bcrypt.gensalt()
            encrypted = bcrypt.hashpw(password, salt).decode()

            User.objects.create(
                name=data['name'],
                email=data['email'],
                password=encrypted,
                phone_number=data['phone_number'],
                address=data['address']
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)


class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "EMAIL ID NOT EXISTS"}, status=401)

            elif User.objects.get(email=data['email']).password != data['password']:
                return JsonResponse({"message": "INVALID PASSWORD"}, status=401)

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


