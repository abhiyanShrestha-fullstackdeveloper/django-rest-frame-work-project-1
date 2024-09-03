from django.db import models

# Create your models here.

class Floor(models.Model):
    name = models.CharField(max_length=255)

class Roomtype(models.Model):
    name = models.CharField(max_length=255)

class Room(models.Model):
    name = models.CharField(max_length=255)
    floor = models.ForeignKey(Floor,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    type = models.ForeignKey(Roomtype,on_delete=models.SET_NULL,null=True)

class Empoyee(models.Model):
    name = models.CharField(max_length=255)
    number = models.BigIntegerField()
    position = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
