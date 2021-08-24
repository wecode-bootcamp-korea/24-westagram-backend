import json
import re

from django.views import View
from django.http import JsonResponse

from postings.models import Posting
from users.models import User

class EnrollmentView(View):

    def post (self,request):
        data = json.loads(request.body)

        try:
            user_id = User.objects.get(
                name=data["user_name"]
            )

            post = Posting.objects.create(
                user        = user_id,
                text        = data["text"],
                img_url     = data["img_url"]
            )
            return JsonResponse({"MESSAGE" : "CREATE"}, status=200)
        
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"MESSAGE" : "VALUE_ERROR"}, status=404)