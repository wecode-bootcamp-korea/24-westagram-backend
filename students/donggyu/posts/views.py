import json

from django.utils.decorators import method_decorator
from django.http             import JsonResponse
from django.views            import View
from django.db.models        import Q

from users.models import User
from .models      import Post, Comment, Like
from .decorator   import login_decorator


@method_decorator(login_decorator, name='dispatch')
class PostCreateView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            user  = request.user
            image = data['image']

            post = Post(
                user  = user,
                image = image 
            )
            post.save()

            return JsonResponse({'MESSAGE': "SUCCESS"}, status=201)

        except ValueError:
            return JsonResponse({'MESSAGE': "VALUE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE': "KEY_ERROR"}, status=400)

class PostListView(View):
    def get(self, request):
        posts = Post.objects.select_related('user').all()

        results = [{
            'id'        : post.id,
            'user'      : post.user.name,
            'image'     : post.image,
            'created_at': post.created_at
            }for post in posts]

        return JsonResponse({'result':results}, status=200)

@method_decorator(login_decorator, name='dispatch')
class UserPostListView(View):
    def get(self, request):
        users  = request.user
        
        results = {
            'post': [
               post.image for post in users.posts.all()
            ]
        }
        return JsonResponse({'result':results}, status=200)

@method_decorator(login_decorator, name='dispatch')
class CommentCreateView(View):
    def post(self, request, post_id):
        try:
            data = json.loads(request.body)
            user = request.user 
            text = data['text']

            if not Post.objects.filter(id=post_id).exists():
                return JsonResponse({'MESSAGE': "INVALID_POST"}, status=400)
            
            post = Post.objects.get(id=post_id)
            comment = Comment(
                user = user,
                post = post, 
                text = text
            )
            comment.save()
                        
            return JsonResponse({'MESSAGE': "SUCCESS"}, status=201)

        except ValueError:
            return JsonResponse({'MESSAGE': "VALUE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE': "KEY_ERROR"}, status=400)
        
class CommentListView(View):
    def get(self, request, post_id):
        if not Post.objects.filter(id=post_id).exists():
                return JsonResponse({'MESSAGE': "INVALID_POST"}, status=400)

        comments = Comment.objects.select_related('post').all()
        results = [{
            'user': comment.user.name,
            'text': comment.text
        }for comment in comments]
        
        return JsonResponse({'result':results}, status=200)

@method_decorator(login_decorator, name='dispatch')
class AddLike(View):
    def post(self, request, post_id):
        
        user = request.user
                    
        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({'MESSAGE': "INVALID_POST"}, status=400)
        
        post = Post.objects.get(id=post_id)

        if Like.objects.filter(Q(user=user.id)&Q(post=post.id)).exists():
            Like.objects.filter(Q(user=user.id)&Q(post=post.id)).delete()
            return JsonResponse({'MESSAGE': "CANCLE_LIKE"}, status=200)

        post.likes.add(user)
        return JsonResponse({'MESSAGE': "ADD_LIKE_SUCCESS"}, status=200)
    
        

