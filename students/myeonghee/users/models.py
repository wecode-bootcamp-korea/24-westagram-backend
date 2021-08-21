from django.db import models

class User(models.Model):

    name        = models.CharField(max_length=45)
    email       = models.EmailField()
    password    = models.CharField(max_length=16)
    cell_number = models.CharField()
    address     = models.CharField()
    birthday	= models.DateField("")
    sex	        = models.DateField("")


    class Meta:
        db_table = "users"
