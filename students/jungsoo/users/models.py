from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=50)
    password     = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique = True)
    ect_info     = models.TextField()

    class Meta:
        db_table = 'users'