from center.forms import CompanyForm
from django.shortcuts import render, redirect
from center.models import Company


def company_view(request):
	if request.method == "POST":
		data = request.POST
		form = CompanyForm(data)
		if form.is_valid():
			form.save()
			msg="company created successfully"
		else:
			msg = form._errors
	else:	
		msg=""
		form = CompanyForm()
	companies = Company.objects.all()
	return render(request, "center/company.html",{"form":form,"message":msg,"companies":companies})
