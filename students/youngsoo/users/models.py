from django.db import models

# Create your models here.
class User(models.Model):
    name          = models.CharField(max_length = 45)
    email         = models.EmailField(max_length = 250, unique=True)
    password      = models.CharField(max_length = 45)
    phone_number  = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    gender        = models.CharField(max_length = 20)
    address       = models.CharField(max_length = 2000)

    class Meta:
        db_table = 'users'

