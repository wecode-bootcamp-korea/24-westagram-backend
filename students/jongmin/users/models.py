from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    phone_id = models.IntegerField()
    etc_info = models.CharField(max_length=200)