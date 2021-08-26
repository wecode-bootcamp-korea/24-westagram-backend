import jwt

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import MY_SECRET_KEY
from users.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try: 
            access_token = request.headers.get("Authorization", None)
            print(access_token)
            payload = jwt.decode(access_token, MY_SECRET_KEY, algorithms="HS256")
            request.user = User.objects.get(id = payload["user"])

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=400)
        
        except ObjectDoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper
