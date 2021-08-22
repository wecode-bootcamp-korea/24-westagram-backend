from django.db import models


class User(models.Model):
    name          = models.CharField(max_length=64)
    email         = models.EmailField()
    password      = models.CharField(max_length=128)
    phone_number  = models.CharField(max_length=32)
    date_of_birth = models.DateField()

    class Meta:
        db_table = "users"
