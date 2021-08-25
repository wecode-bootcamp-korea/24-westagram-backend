import json
import re

from django.views import View
from django.http import JsonResponse

from postings.models import Posting, PostingComment
from users.models import User

class EnrollmentView(View):

    def post (self,request):
        data = json.loads(request.body)

        try:
            post_user = User.objects.get(
                name = data["user_name"]
            )
            Posting.objects.create(
                text         = data["text"],
                img_url      = data["img_url"],
                posting_user = post_user
            )

            return JsonResponse({"MESSAGE" : "CREATE"}, status=200)
        
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"MESSAGE" : "VALUE_ERROR"}, status=404)

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            comment_user_1 = User.objects.get(name=data["comment_user"])
            posting_1      = Posting.objects.get(id=data["post_id"])
            
            PostingComment.objects.create(
               comment      = data["comment"],
               posting      = posting_1,
               comment_user = comment_user_1
            )
            return JsonResponse({"MESSAGE" : "CREATE"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"MESSAGE" : "VALUE_ERROR"}, status=404)

    def get(self, request):
        
        try:
            #1번 게시물의 댓글 리스트
            comments_list = []
            result        = []
            comments      = PostingComment.objects.filter(posting_id=1)

            for comment in comments:
                comments_list.append({
                    "comment"       : comment.comment,
                    "comment_user"  : comment.comment_user_id,
                    "comment_time"  : comment.comment_time
                })

            result.append({
                "post_id" : 1,
                "comment" : comments_list
            })
            
            return JsonResponse({"MESSAGE" : "CREATE", "RESULTS": result}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"MESSAGE" : "VALUE_ERROR"}, status=404)



    

