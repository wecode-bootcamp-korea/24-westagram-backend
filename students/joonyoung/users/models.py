from django.db import models


class User(models.Model):
    name          = models.CharField(max_length=30)
    email         = models.EmailField()
    password      = models.CharField(max_length=200)
    phone_number  = models.CharField(max_length=15)
    bio           = models.TextField(default="", blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name
