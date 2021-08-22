from django.db import models


class User(models.Model):
    user_name    = models.CharField(max_length=30)
    email        = models.EmailField(max_length=50)
    password     = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=20)
    address      = models.CharField(max_length=100)
    created      = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ['created']