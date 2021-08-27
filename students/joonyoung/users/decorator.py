import jwt

from django.http import JsonResponse

from my_settings import SECRET_KEY, ALGORITHM
from .models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.META["HTTP_AUTHORIZATION"]
            if not token:
                return JsonResponse({"message": "NEED_LOGIN"}, status=400)

            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
            user          = User.objects.get(id=decoded_token.get("user_id"))
            request.user  = user
            
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "JWT_PROBLEM"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "USER_DOES_NOT_EXITS"}, status=400)
        except KeyError:
            return JsonResponse({"message": "DO_NOT_HAVE_TOKEN"}, status=400)
        
        return func(self, request, *args, **kwargs)
        
    return wrapper