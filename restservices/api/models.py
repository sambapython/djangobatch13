from django.db import models

# Create your models here.
class Category(models.Model):
	name= models.CharField(max_length=250)

class Product(models.Model):
	name = models.CharField(max_length=250)
	cost = models.FloatField(default=0.0)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
