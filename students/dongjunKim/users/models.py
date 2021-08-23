from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=30)
    email    = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    phone    = models.CharField(max_length=25)
    
    class Meta:
        db_table = 'users'
