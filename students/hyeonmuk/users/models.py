from django.db import models


class User(models.Model):
    name           = models.CharField(max_length=40)
    email          = models.CharField(max_length=40)
    password       = models.CharField(max_length=200)
    contact_mobile = models.CharField(max_length=20)
    nickname       = models.CharField(max_length=40)
    address        = models.CharField(max_length=300)

    class Meta:
        db_table   = 'users'
