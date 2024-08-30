from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    address = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)


