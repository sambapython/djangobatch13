from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import Category, Product
from rest_framework.serializers import ModelSerializer, ValidationError

class PutModelSerializer(ModelSerializer):
	def __init__(self,*args,**kwargs):
		ModelSerializer.__init__(self,*args,**kwargs)
		self.partial=True

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product 
		fields = "__all__"
	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("Name not valid")
		return value

class ProductPutSerializer(PutModelSerializer):
	class Meta:
		model = Product 
		fields = "__all__"

	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("Name not valid")
		return value

class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get_serializer_class(self):
		method = self.request.method.lower()
		if method == "put":
			return ProductPutSerializer
		return self.serializer_class

class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = "__all__"
	def validate_name(self,value):
		if not value.isalnum():
			raise ValidationError("Name not valid")
		return value

# Create your views here.
class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer