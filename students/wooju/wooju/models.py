from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=45)
    email         = models.CharField(max_length=300)
    password      = models.CharField(max_length=45)
    phone_number  = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        db_table  = 'users'