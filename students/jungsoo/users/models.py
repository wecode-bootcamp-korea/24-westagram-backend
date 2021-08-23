from django.db import models

# Create your models here.

from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    information = models.TextField()

    class Meta:
        db_table = 'users'