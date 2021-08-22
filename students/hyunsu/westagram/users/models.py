from django.db import models

# Create your models here.
class User(models.Model):
    name          = models.CharField(max_length=20)
    email         = models.EmailField(max_length=100)
    password      = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=20)
    address       = models.CharField(max_length=100)

    class Meta:
        db_table = "users"
