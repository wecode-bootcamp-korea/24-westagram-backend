from django.db   import models
from phone_field import PhoneField

# Create your models here.

class User(models.Model):
    first_name    = models.CharField(
            max_length = 10,  
            blank      = False
            )
    last_name     = models.CharField(
            max_length = 10,  
            blank      = False
            )
    email         = models.EmailField(
            max_length = 50, 
            blank      = False
            )
    password      = models.CharField(
            max_length = 100, 
            blank      = False
            )
    phone_number  = PhoneField(
            blank      = False
            )
    gender_choice =(
            ('M', 'Man'),
            ('W', 'Woman')
            )
    gender        = models.CharField(
            max_length = 1,
            choices    = gender_choice
            )
    birth         = models.DateField(
            )
    
