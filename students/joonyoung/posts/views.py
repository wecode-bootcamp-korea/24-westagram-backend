import json
from json.decoder import JSONDecodeError
from users.decorator import login_decorator

from django.http import JsonResponse
from django.views import View
from django.db.models import Q

from posts.models import Post, Image, Comment, Like, Follow
from users.models import User
from users.decorator import login_decorator

class AddPostingView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            caption  = data["caption"]
            img_urls = data["url"]
            location = data.get("location")

            post = Post.objects.create(
                caption  = caption,
                user_id  = request.user.id,
                location = location,
            )
            img_list = []
            for img_url in img_urls:
                image = Image.objects.create(url=img_url, post_id=post.id)
                img_list.append(image.url)

            created_post = {
                "id"      : post.id,
                "caption" : post.caption,
                "user"    : post.user.name,
                "img_url" : img_list,
                }

            return JsonResponse({"Message": "SUCCESS CREATE", "Result": created_post}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)


    def get(self, request):
        posts     = Post.objects.all()
        post_list = []

        for post in posts:
            img_list = []
            for img in post.image.all():
                img_list.append(img.url)
            
            post_list.append(
                {
                    "post_caption" : post.caption,
                    "post_user"    : post.user.name,
                    "posting_date" : (post.posting_time).strftime("%Y-%m-%d %I:%M %p"),
                    "post_img"     : img_list,
                }
            )

        return JsonResponse({"Result": post_list}, status=201)

class UserPostingView(View):
    @login_decorator
    def get(self, request, user_id):
        if not User.objects.filter(id=user_id).exists():
            return JsonResponse({"message": "USER_DOES_NOT_EXIST"}, status=400)
        
        posts     = Post.objects.filter(user_id=user_id)
        post_list = []

        for post in posts:
            img_list = []
            for img in post.image.all():
                img_list.append(img.url)
            
            post_list.append(
                {
                    "post_caption" : post.caption,
                    "post_user"    : post.user.name,
                    "posting_date" : (post.posting_time).strftime("%Y-%m-%d %I:%M %p"),
                    "post_img"     : img_list,
                }
            )

        return JsonResponse({"Result": post_list}, status=200)

class PostingView(View):
    @login_decorator
    def delete(self, request, post_id):
        if Post.objects.filter(id=post_id).exists():
            post = Post.objects.get(id=post_id)
            if post.user.id == request.user.id:
                post.delete()
                return JsonResponse({"message": "SECCESS_DELETE"}, status=200)
            return JsonResponse({"message": "YOU_ARE_NOT_POSTING_USER"}, status=400)
        return JsonResponse({"message": "POST_DOES_NOT_EXIST"}, status=400)
    
    @login_decorator
    def put(self, request, post_id):
        try:
            data = json.loads(request.body)

            caption  = data["caption"]
            location = data.get("location")

            if Post.objects.filter(id=post_id).exists():
                if Post.objects.get(id=post_id).user.id == request.user.id:
                    Post.objects.filter(id=post_id).update(
                        caption  = caption,
                        location = location,
                    )

                    updated_post = {
                        "id"      : Post.objects.get(id=post_id).id,
                        "caption" : Post.objects.get(id=post_id).caption,
                        "user"    : Post.objects.get(id=post_id).user.name,
                        }
                    return JsonResponse({"Message": "SUCCESS_UPDATE", "Result": updated_post}, status=201)
                return JsonResponse({"message": "YOU_ARE_NOT_POSTING_USER"}, status=400)
            return JsonResponse({"message": "POST_DOES_NOT_EXIST"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)

class AddCommentView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            comment           = data["comment"]
            post_id           = data["post_id"]
            parent_comment_id = data.get("parent_comment_id")

            if Post.objects.filter(id=post_id).exists():
                created_comment = Comment.objects.create(
                    comment           = comment, 
                    post_id           = post_id, 
                    user_id           = request.user.id,
                    parent_comment_id = parent_comment_id,
                )
                comment = {
                    "comment" : created_comment.comment,
                    "user" : created_comment.user.name,
                    "post" : created_comment.post.id,
                    "parrent_comment" : created_comment.parent_comment_id,
                    "commenting_time" : created_comment.commenting_time.strftime("%Y-%m-%d %I:%M %p"),
                }
                return JsonResponse({"message": "SECCESS_ADD_COMMENT", "Result" : comment}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)

class CommentView(View):
    @login_decorator
    def delete(self, request, comment_id):
        if Comment.objects.filter(id=comment_id).exists():
            comment = Comment.objects.get(id=comment_id)
            if comment.user.id == request.user.id:
                comment.delete()
                return JsonResponse({"message": "SECCESS_DELETE"}, status=200)
            return JsonResponse({"message": "YOU_ARE_NOT_COMMENT_USER"}, status=400)
        return JsonResponse({"message": "COMMENT_DOES_NOT_EXIST"}, status=400)

    @login_decorator
    def put(self, request, comment_id):
        try:
            data = json.loads(request.body)

            comment = data["comment"]

            if Comment.objects.filter(id=comment_id).exists():
                if Comment.objects.get(id=comment_id).user.id == request.user.id:
                    Comment.objects.filter(id=comment_id).update(comment=comment)

                    updated_post = {
                        "id"              : Comment.objects.get(id=comment_id).id,
                        "comment"         : Comment.objects.get(id=comment_id).comment,
                        "user"            : Comment.objects.get(id=comment_id).user.name,
                        "post"            : Comment.objects.get(id=comment_id).post.id,
                        "parrent_comment" : Comment.objects.get(id=comment_id).parent_comment_id,
                        }
                    return JsonResponse({"Message": "SUCCESS_UPDATE", "Result": updated_post}, status=201)
                return JsonResponse({"message": "YOU_ARE_NOT_POSTING_USER"}, status=400)
            return JsonResponse({"message": "POST_DOES_NOT_EXIST"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)
            
class PostcommentingView(View):
    def get(self, request, post_id):
        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({"message": "POST_DOES_NOT_EXIST"}, status=400)
        
        comments     = Comment.objects.filter(post_id=post_id)
        comment_list = []

        for comment in comments:
            comment_list.append(
                {
                    "comment"         : comment.comment,
                    "commenting_time" : comment.commenting_time.strftime("%Y-%m-%d %I:%M %p"),
                    "user"            : comment.user.name,
                    "parent_comment"  : comment.parent_comment_id,
                }
            )
        
        return JsonResponse({"Result": comment_list}, status=200)

class ToggleLikeView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            user_id = request.user.id
            post_id = data["post_id"]

            if Like.objects.filter(Q(user_id=user_id) & Q(post_id=post_id)).exists():
                Like.objects.filter(Q(user_id=user_id) & Q(post_id=post_id)).delete()
                return JsonResponse({"message": "DELETE_LIKE"}, status=200)

            Like.objects.create(user_id=user_id, post_id=post_id)
            return JsonResponse({"message": "ADD_LIKE"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)

class ToggleFollowView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            follower_id  = request.user.id
            following_id = data["following_id"]

            if Follow.objects.filter(Q(follower_id=follower_id) & Q(following_id=following_id)).exists():
                Follow.objects.filter(Q(follower_id=follower_id) & Q(following_id=following_id)).delete()
                return JsonResponse({"message": "DELETE_FOLLOW"}, status=200)

            Follow.objects.create(follower_id=follower_id, following_id=following_id)
            return JsonResponse({"message": "ADD_FOLLOW"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)