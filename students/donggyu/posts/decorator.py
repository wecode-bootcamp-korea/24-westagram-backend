import jwt
import json

from django.http.response import JsonResponse

from users.models import User
from my_settings import SECRET_KEY

def login_decorator(func):
    def wraper(request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            token = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=token['id'])
            request.user = user
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE': 'ENCODE_ERROR'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)

        return func(request, *args, **kwargs)
    
    return wraper

