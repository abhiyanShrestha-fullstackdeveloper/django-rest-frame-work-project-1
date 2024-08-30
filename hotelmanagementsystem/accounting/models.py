from django.db import models

# Create your models here.

class Bills(models.Model):
    description = models.TextField()
    totalamount = models.FloatField()

class Payment(models.Model):
    paidamount = models.FloatField()

class Employeesalary(models.Model):
    paidamount = models.FloatField()