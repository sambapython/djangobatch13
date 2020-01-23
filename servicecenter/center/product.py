from django.shortcuts import render, redirect
from center.models import Product

from django.views.generic import TemplateView
class ProductTemplateView(TemplateView):
	def get_context_data(self):
		context = TemplateView.get_context_data(self)
		context.update({"products":Product.objects.all()})
		return context