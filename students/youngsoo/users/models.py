from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone_num = models.IntegerField()
    other_info = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

