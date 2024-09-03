from django.db import models
from management.models import Room
# Create your models here.

class Foodcategory(models.Model):
    name = models.CharField(max_length=250)

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Foodcategory,on_delete=models.SET_NULL,null=True)
    menu = models.ForeignKey('Menu',on_delete=models.SET_NULL,null=True)
    
class Order(models.Model):
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    food = models.ForeignKey(Food,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    table = models.ForeignKey('Table',on_delete=models.SET_NULL,null=True)
    
    
class Table(models.Model):
    name = models.CharField(max_length=255)
    is_empty = models.BooleanField(null=True)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    
class Resturantbill(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    customername = models.CharField(max_length=255)
    customenumber = models.BigIntegerField()
    totalamount = models.FloatField()
    paidamount = models.FloatField()