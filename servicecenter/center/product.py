from django.shortcuts import render, redirect
from center.models import Product
from center.forms import ProductForm
from django.core.paginator import Paginator
from django.conf import settings

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from center.models import Product

class ProductCreateView(CreateView):
	model=Product
	fields=['name',"description","company","image"]
	success_url="/product"

	def post(self, request, *args, **kwargs):
		resp = super().post(request, *args, **kwargs)
		obj = self.object 
		obj.createdby = request.user 
		obj.save()
		return resp


@login_required
def productlist(request):
	params = request.GET
	all_products=Product.objects.all()
	form = ProductForm()
	page_num = params.get("page") or 1
	if params:
		#import pdb;pdb.set_trace()
		form = ProductForm(data=params)
		name=params.get("name")
		description = params.get("description")
		company = params.get("company")
		if name:
			#all_products = all_products.filter(name=name) # exact: case sensitive search
			#all_products = all_products.filter(name__iexact=name) # iexact: case insensitive search
			all_products = all_products.filter(name__contains=name)
		if description:
			all_products = all_products.filter(description__contains=description)
		if company:
			all_products = all_products.filter(company__name__contains=company)
	page_count = settings.PAGE_COUNT
	# if not page_num:
	# 	page_num=1
	paginator_object = Paginator(all_products,page_count)
	page = paginator_object.page(page_num)
	return render(request,"center/product_list.html",{"page_object":page,"paginator":paginator_object,"form":form})
class ProductTemplateView(TemplateView):
	def get_context_data(self):
		context = TemplateView.get_context_data(self)
		context.update({"products":Product.objects.all()})
		return context