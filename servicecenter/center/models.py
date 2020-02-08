from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login,logout,authenticate
class BaseAbstract(models.Model):
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	createdby  = models.ForeignKey("UserProfile", related_name="%(class)s_created",on_delete=models.PROTECT,
		null=True,blank=True)
	updatedby = models.ForeignKey("UserProfile",related_name="%(class)s_updated",on_delete=models.PROTECT,
		null=True,blank=True)

	class Meta:
		abstract=True
class RequestTracker(models.Model):
	client_ip = models.CharField(max_length=250, blank=True,null=True)
	request_url = models.CharField(max_length=250, blank=True,null=True)
	resp_code = models.CharField(max_length=250, blank=True,null=True) 

class NameAbstract(models.Model):
	# abstract model
	name = models.CharField(max_length=61)
	class Meta:
		abstract = True

class UserProfile(AbstractUser):
	password = models.CharField(max_length=250, blank=True, null=True)
	phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
	address = models.TextField(blank=True, null=True)



class UserType(NameAbstract):
	pass
	#name = models.CharField(max_length=61)
class Company(BaseAbstract):
	name = models.CharField(max_length=61, unique=True)
	description = models.CharField(max_length=250, default="")
	owner = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.PROTECT)
	address = models.CharField(max_length=250 ,default="")

	def __str__(self):
		return "%s:%s"%(self.name,self.description)

class Product(NameAbstract, BaseAbstract):
	description = models.TextField(default="")
	company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True,)
	image = models.FileField(blank=True, null=True)

class Customer(models.Model):
	name = models.CharField(max_length=250)
	image = models.FileField()





























