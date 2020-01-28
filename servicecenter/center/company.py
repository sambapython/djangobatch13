from center.forms import CompanyForm, companySearchForm
from django.shortcuts import render, redirect
from center.models import Company
from django.views.generic import ListView
from django.conf import settings
from django.contrib.auth.decorators import login_required
class CompanyListView(ListView):
	model = Company
	paginate_by=settings.PAGE_COUNT
	#queryset  = Company.objects.all()
	def get_queryset(self):
		q=Company.objects.all()
		params = self.request.GET 
		name = params.get("name")
		description = params.get("description")
		owner = params.get("owner")
		address = params.get("address")
		if name:
			q=q.filter(name__icontains=name)
		if description:
			q=q.filter(description__icontains=description)
		if owner:
			q=q.filter(owner__name__icontains=owner)
		if address:
			q=q.filter(address__icontains=address)
		return q

	def get_context_data(self,*args,**kwargs):
		data = ListView.get_context_data(self,*args,**kwargs)
		q=self.get_queryset()
		params = self.request.GET
		form = companySearchForm()
		if params:
			form = companySearchForm(data=params)
		data.update({"companies":q,"form":form,"perpage":self.paginate_by})
		return data
@login_required
def company_view_delete(request,pk):
	data = Company.objects.filter(id=pk)
	msg=""
	form= ""
	if data:
		company = data[0]
		form = CompanyForm(instance=company)
		if request.method=="POST": 
			data.delete()
			msg="form deleted successfully"
			return redirect("/company")
	else:
		msg="company not found"
	return render(request,"center/companyform_confirm.html",{"form":form,"message":msg})
@login_required
def company_view_update(request,pk):
	data = Company.objects.filter(id=pk)
	msg=""
	form= ""
	if data:
		company = data[0]
		form = CompanyForm(instance=company)
		if request.method=="POST":
			new_data = request.POST
			form = CompanyForm(instance=company, data=new_data) 
			if form.is_valid():
				form.save()
				msg="form updated successfully"
				return redirect("/company")
			else:
				msg=form._errors
	else:
		msg="company not found"
	return render(request,"center/companyform.html",{"form":form,"message":msg})
@login_required
def company_create_view(request):
	if request.method == "POST":
		data = request.POST
		form = CompanyForm(data)
		if form.is_valid():
			form.save()
			msg="company created successfully"
			return redirect("/company")
		else:
			msg = form._errors
	else:	
		msg=""
		form = CompanyForm()
	return render(request,"center/companyform.html",{"form":form,"message":msg})
@login_required
def company_view(request):
	
	companies = Company.objects.all()
	return render(request, "center/company.html",{"companies":companies})
