from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name     = models.CharField(max_length=45)
    email    = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone    = PhoneNumberField(max_length=17, null=True, blank=True)
    nickname = models.CharField(max_length=45, unique=True)

    class Meta():
        db_table = 'users'

class Comment(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    comment = models.CharField(max_length=500)

    class Meta():
        db_table = 'comments'