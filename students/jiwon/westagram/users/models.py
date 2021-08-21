from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=45)
    cellphone = models.CharField(max_length=45)
    favorite_food = models.CharField(max_length=80)
    
    class Meta:
        db_table = 'users' #데이터베이스 table 네임 지정