  1 import json
  2 import re
  3 import bcrypt
  4 
  5 from django.http import JsonResponse
  6 from django.views import View
  7 
  8 from users.models import User
  9 
 10 class LoginView(View) :
 11     def post(self, request) :
 12         try :
 13             data = json.loads(request.body)
 14 
 15             if not User.objects.filter(email=data['email']).exists() :
 16                 return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
 17 
 18             user = User.objects.get(email=data['email'])
 19 
 20             if user.password != data['password'] :
 21                 return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
 22 
 23             return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
 24 
 25 class SignupView(View) :
 26     def post(self, request) :
 27         try :
 28             data = json.loads(request.body)
 29 
 30             if not re.compile('^[a-zA-Z0-9!#$%^&*()]+@[a-z]+.[a-z]+$').match(data['email']) :
 31                 return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'},status=400)
 32 
 33             if not re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,100}$').match(data['password']) :
 34                 return JsonResponse({'MESSAGE':'INVALID_PASSWORD_ERROR'},status=400)
 35 
 36             if User.objects.filter(email=data['email']).exists() :
 37                 return JsonResponse({'MESSAGE':'DUPLICATION_ERROR'}, status=400)
 38 
 39             hashed_password = bcrypt.hashpw( data['password'].encode('utf-8'), bcrypt.gensalt() )
 40             
 41             User.objects.create(
 42                 name     = data['name'],
 43                 email    = data['email'],
 44                 password = hashed_password.decode(),
 45                 phone    = data['phone']
 46             )   
 47             return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
 48             
 49         except KeyError :
 50             return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400) 
~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~                                                                                         
