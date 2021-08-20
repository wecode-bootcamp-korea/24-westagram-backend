from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=128)
    email        = models.EmailField(unique=True)
    password     = models.CharField(max_length=2048)
    phone_number = models.CharField(max_length=32)
    address      = models.CharField(max_length=256)