from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,default='username')
    image = models.ImageField()
    location = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Customer(models.Model):
    name = models.CharField(max_length=255)
    number = models.BigIntegerField()
    address = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)


