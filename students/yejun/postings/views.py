import json

from django.http import JsonResponse
from django.views import View

from .models import Posting, ImageURL
from users.models import User
from core.utils import login_decorator


class PostingView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            new_post = Posting.objects.create(
                feed_text=data["feed_text"], user=request.user
            )

            for image_url in data["image_url"]:
                ImageURL.objects.create(image_url=image_url, postings=new_post)
            return JsonResponse({"messgae": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    @login_decorator
    def get(self, request):
        result = []
        postings = Posting.objects.all()

        for posting in postings:
            image_urls = ImageURL.objects.filter(postings=posting.id)
            result.append(
                {
                    "feed_text": posting.feed_text,
                    "created_time": posting.created_time,
                    "user": posting.user_id,
                    "image_urls": list(image_urls.values()),
                }
            )
        return JsonResponse({"results": result}, status=200)
