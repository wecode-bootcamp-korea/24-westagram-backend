from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from users.models import User
from django.db.utils import IntegrityError
import json
import re


# Create your views here.
class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        def is_email_valid(email):
            email_valid = re.search('[a-zA-Z0-9.+-]+@'
                                    '[a-zA-Z0-9-]+\.'
                                    '[a-zA-Z0-9.]+', email)
            if email_valid:
                return email
            raise IntegrityError             

        def is_password_valid(password):
            password_valid = re.fullmatch('^(?=.*[a-z])(?=.*[A-Z])'
                                          '(?=.*\d)(?=.*[@$!%*?&])'
                                          '[A-Za-z\d@$!%*?&]{8,32}$', password)
            if password_valid:
                return password
            raise IntegrityError
            
        try:
            user = User.objects.create(
                name          = data['name'],
                email         = is_email_valid(data['email']),
                password      = is_password_valid(data['password']),
                phone_number  = data['phone_number'],
                date_of_birth = data['date_of_birth'],
                gender        = data['gender'],
                address       = data['address'],
            )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except IntegrityError:
            return JsonResponse({"message" : "INVALID EMAIL OR PASSWORD"}, status = 400)
        
            

        
        



    
        

