from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    gender       = models.CharField(max_length=45)
    address      = models.CharField(max_length=200)
    birth        = models.DateField()
    email        = models.CharField(max_length=100)
    password     = models.CharField(max_length=150)
    