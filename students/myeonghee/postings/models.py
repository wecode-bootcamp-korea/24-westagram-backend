from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField

from users.models import User

class Posting(models.Model):
    
    user         = models.ManyToManyField(User, through ="PostingComment", related_name='user')
    posting_date = models.DateField(auto_now_add=True)
    text         = models.CharField(max_length=500)
    img_url      = models.CharField(max_length=100)
    posting_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "postings"

class PostingComment(models.Model):

    comment      = models.CharField(max_length=100)
    posting      = models.ForeignKey("Posting", on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "postings_comments"