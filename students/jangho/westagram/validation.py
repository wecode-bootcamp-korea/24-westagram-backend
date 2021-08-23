from django.http import JsonResponse, HttpResponse
import re


def email_validation(data) -> bool:
    em_val = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    try:
        res_val = em_val.search(data['email'])
        if not res_val:
            return JsonResponse({'message': 'INVALID_EMAIL_FORMAT'}, status=400)
    except:
        return JsonResponse({'message': 'INVALID_EMAIL_FORMAT'}, status=400)

def nickname_validation(data) -> bool:
    em_val = re.compile(r'^[a-zA-Z0-9+-_.]')
    try:
        res_val = em_val.match(data['nickname'])
        if not res_val:
            return JsonResponse({'message': 'INVALID_NICKNAME_FORMAT'}, status=400)
    except:
        return JsonResponse({'message': 'INVALID_NICKNAME_FORMAT'}, status=400)

def pw_validation(data) -> bool:
    pw_val = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
    try:
        res_val = pw_val.match(data['password'])
        if not res_val:
            return JsonResponse({'message': 'INVALID_PASSWORD_FORMAT'}, status=400)
    except:
        return JsonResponse({'message': 'ERROR'}, status=400)