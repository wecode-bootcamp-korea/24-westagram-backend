import json

from django.http             import JsonResponse
from django.views            import View
from django.utils.decorators import method_decorator

from users.models import User
from .models       import Post
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



        