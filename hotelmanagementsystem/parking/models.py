from django.db import models
from frontdesk.models import Customer
# Create your models here.

class Parkingsections(models.Model):
    name = models.CharField(max_length=255)

class Ticketcharges(models.Model):
    charge = models.FloatField()
    ticket = models.ForeignKey('Ticket',on_delete=models.SET_NULL,null=True)

class Ticket(models.Model):
    guestname = models.CharField(max_length=255)
    guestnumber = models.BigIntegerField()
    section = models.ForeignKey(Parkingsections,on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)