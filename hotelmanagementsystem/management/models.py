from django.db import models

# Create your models here.

class Floor(models.Model):
    name = models.CharField(max_length=255)

class Roomtype(models.Model):
    name = models.CharField(max_length=255)

class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Empoyee(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    position = models.CharField(max_length=255)
    address = models.TextField()

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
