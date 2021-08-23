from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=45)
    email        = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    gender       = models.CharField(max_length=45)
    address      = models.CharField(max_length=200)
    birth        = models.DateField()





    