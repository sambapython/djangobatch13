from django.shortcuts import render, redirect
from center.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
	msg=""
	if request.method.lower()=="post":
		data= request.POST
		user = UserProfile(username=data.get("email"),
					email=data.get("email"),
					password=data.get("password"),
					address = data.get("address"),
					phone=data.get("phone"))
		try:
			user.save()
			# to encrypt the password
			user.set_password(data.get("password"))
			user.save()
			msg="user created successfully"
		except Exception as err:
			msg = str(err)
	return render(request,"center/signup.html",{"message":msg})
def signin_view(request):
	msg=""
	method = request.method.lower()
	if method=="post":
		data= request.POST
		username = data.get("email")
		password = data.get("password")
		#user = UserProfile.objects.filter(username=username, password=password)
		user = authenticate(username=username,password=password)
		if user:
			login(request, user)
			msg="authenticated"
			next_url = request.GET.get("next","/") 
			return redirect(next_url)
		else:
			msg="not authenticated"
	return render(request,"center/signin.html",{"message":msg})
@login_required
def signout_view(request):
	logout(request)
	return redirect("/")
def home_view(request):
	msg=""		
	return render(request,"center/home.html",{"message":msg})
