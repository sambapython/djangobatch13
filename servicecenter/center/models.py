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
class Company(NameAbstract):
	description = models.CharField(max_length=250, default="")
	owner = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.PROTECT)
	address = models.CharField(max_length=250 ,default="")

class Product(NameAbstract):
	description = models.TextField(default="")
	company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True,)





























