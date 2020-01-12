from django.db import models

# Create your models here.
class UserType(models.Model):
	name = models.CharField(max_length=61)

