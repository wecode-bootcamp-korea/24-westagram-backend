from django.db import models

class User(models.Model):
    GENDER = (
        ('M', 'MAN'),
        ('W', 'WOMAN')
    )
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'users'
