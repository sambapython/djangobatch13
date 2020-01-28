
from django import forms
from center.models import Company, Product
class companySearchForm(forms.Form):
	name=forms.CharField(max_length=250,required=False)
	description = forms.CharField(max_length=250,required=False)
	owner = forms.CharField(max_length=250,required=False)
	address = forms.CharField(max_length=250,required=False)
class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = "__all__"
	def clean_name(self,*args,**kwargs):
		name = self.data.get("name")
		if name.isalnum():
			return name 
		else:
			raise forms.ValidationError("name not valid")
	#def clean_address(self):
	#def clean_description(self):
class ProductForm(forms.Form):
	name = forms.CharField(max_length=250,required=False)
	description = forms.CharField(max_length=250,required=False)
	company = forms.CharField(max_length=250,required=False)
	page = forms.IntegerField(required=False)
	class Meta:
		model=Product
		fields="__all__"

	