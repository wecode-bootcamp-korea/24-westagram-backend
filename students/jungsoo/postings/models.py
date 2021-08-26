from datetime import datetime

from django.db import models

from users.models import User

class Posting(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500)

    class Meta:
        db_table = 'postings'
