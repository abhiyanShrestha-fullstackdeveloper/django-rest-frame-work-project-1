from django.db import models

# Create your models here.

class Parkingsections(models.Model):
    name = models.CharField(max_length=255)

class Ticketcharges(models.Model):
    charge = models.FloatField()

class Ticket(models.Model):
    guestname = models.CharField(max_length=255)
    guestnumber = models.IntegerField()