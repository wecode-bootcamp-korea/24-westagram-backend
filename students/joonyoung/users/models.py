from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    bio = models.TextField(default="", blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name
