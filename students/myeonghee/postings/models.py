from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

from users.models import User

class Posting(models.Model):

    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    posting_date = models.DateField(auto_now_add=True)
    text         = models.CharField(max_length=500)
    img_url      = models.CharField(max_length=100)

    class Meta:
        db_table = "postings"