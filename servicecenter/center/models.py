from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login,logout,authenticate

class NameAbstract(models.Model):
	# abstract model
	name = models.CharField(max_length=61)
	class Meta:
		abstract = True

class UserProfile(AbstractUser):
	phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
	address = models.TextField(blank=True, null=True)



class UserType(NameAbstract):
	pass
	#name = models.CharField(max_length=61)






























# Create your models here.


class Parent(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField()

class Child(Parent):
	# one to one relation to parent
	phone = models.CharField(max_length=25)
	address = models.TextField(default="address sample")


class Product(NameAbstract):
	#name = models.CharField(max_length=60)
	cost = models.FloatField()
	description = models.TextField(blank=True, null=True) #None
class Customer(NameAbstract):
	#name = models.CharField(max_length=60)
	address = models.TextField()
	email = models.EmailField(unique=True)
	phone = models.CharField(unique=True, max_length=60)
class SalesOrders(models.Model):
	description = models.TextField(blank=True, null=True)
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	products = models.ManyToManyField(Product)


