from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=45)
    email       = models.EmailField()
    password    = models.CharField(max_length=200)
    contact     = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'users'
