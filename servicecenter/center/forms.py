
from django import forms
from center.models import Company
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
	