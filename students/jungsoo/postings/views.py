import json

from django.views import View
from django.http import JsonResponse

from postings.models import Posting
from users.models import User

class InputView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            Posting.objects.create(
                user         = User.objects.get(name=data['user']), 
                created_time = data['created_time'], 
                image_url    = data['image_url'], 
            )
            return JsonResponse({'MESSAGE':'CREATED'}, status=201)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

class OutputView(View):
    def get(self, request):
