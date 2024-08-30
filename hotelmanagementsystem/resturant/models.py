from django.db import models

# Create your models here.

class Foodcategory(models.Model):
    name = models.CharField(max_length=250)

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
class Order(models.Model):
    quantity = models.IntegerField()
    
class Table(models.Model):
    name = models.CharField(max_length=255)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    
class Resturantbill(models.Model):
    customername = models.CharField(max_length=255)
    customenumber = models.IntegerField()
    totalamount = models.FloatField()
    paidamount = models.FloatField()