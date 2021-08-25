import json

from django.http  import JsonResponse
from django.views import View

from postings.models import Posting

class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)
        Posting.objects.create(
            post_time = data['post_time'],
            image     = data['image_url'],
            user_id   = data['user_id'],
            )

        return JsonResponse({'MESSAGE' : 'POSTED'}, status = 201)

class PostingGet(View):
    def get(self, request):
        post = list(Posting.objects.values())
        return JsonResponse({
            'MESSAGE' : post}, status = 201)
        

