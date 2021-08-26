from django.db import models
 
# Create your models here.

class Posting(models.Model):
    user      = models.ForeignKey('users.User', on_delete = models.CASCADE)
    post_time = models.DateField(auto_now_add = True)
    image     = models.CharField(max_length = 1000)

    class Meta:
        db_table = 'postings'

