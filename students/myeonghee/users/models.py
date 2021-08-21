from django.db import models

class User(models.Model):

    name        = models.CharField(max_length=45)
    email       = models.EmailField()
    password    = models.CharField(max_length=16)
    cell_number = models.CharField(max_length=13)
    address     = models.CharField(max_length=50)
    birthday	= models.DateField("")
    sex	        = models.CharField(max_length=2)


    class Meta:
        db_table = "users"
