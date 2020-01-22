from center.forms import CompanyForm
from django.shortcuts import render, redirect
from center.models import Company
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
def company_view(request):
	
	companies = Company.objects.all()
	return render(request, "center/company.html",{"companies":companies})
