from django.db import models

class User(models.Model):

    name        = models.CharField(max_length=45)
    email       = models.EmailField()
    password    = models.CharField(max_length=16)
    cell_number = models.IntegerField(default=0)
    private_info     = models.CharField()

    class Meta:
        db_table = "Users"














