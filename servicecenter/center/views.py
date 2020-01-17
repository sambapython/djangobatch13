from django.shortcuts import render
from center.models import UserProfile
from django.contrib.auth import authenticate

# Create your views here.
def home_view(request):
	msg=""
	method = request.method.lower()
	if method=="post":
		data= request.POST
		if "signup" in data:
			user = UserProfile(username=data.get("email"),
				email=data.get("email"),
				password=data.get("password"),
				address = data.get("address"),
				phone=data.get("phone"))
			try:
				user.save()
				user.set_password(data.get("password"))
				user.save()
				msg="user created successfully"
			except Exception as err:
				msg = str(err)
		elif "signin" in data:
			data = request.POST 
			username = data.get("email")
			password = data.get("password")
			#user = UserProfile.objects.filter(username=username, password=password)
			user = authenticate(username=username,password=password)
			if user:
				msg="authenticated"
			else:
				msg="not authenticated"
			
	return render(request,"center/home.html",{"message":msg})
