from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField, EmailField
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name     = models.CharField(max_length=45)
    email    = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone = PhoneNumberField(max_length=17, null=False, blank=False, unique=True)


    class Meta():
        db_table = 'users'