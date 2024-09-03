from django.db import models
from frontdesk.models import Customer
from management.models import Empoyee
# Create your models here.

class Bills(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    totalamount = models.FloatField()

class Payment(models.Model):
    bill = models.OneToOneField(Bills,on_delete=models.SET_NULL,null=True)
    paidamount = models.FloatField()

class Employeesalary(models.Model):
    employee = models.ForeignKey(Empoyee,on_delete=models.SET_NULL,null=True)
    paidamount = models.FloatField()