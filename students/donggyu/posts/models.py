from typing import Text
from django.db    import models
from users.models import User

class Post(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image      = models.URLField(max_length=2048)
    text       = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

class Comment(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'
