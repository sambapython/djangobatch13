from django.shortcuts import render, redirect
from center.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from django.http import HttpResponse

# Create your views here.
def googleauth(request, *args, **kwargs):
	import pdb;pdb.set_trace()
def googlesignin(request):
	# goto google take the login screen
	# to do this need to call google api
	token_request_uri = "https://accounts.google.com/o/oauth2/auth"
	response_type = "code"
	client_id = settings.GOOGLE_CLIENT_ID
	redirect_uri = "http://127.0.0.1:8000/googleauth"
	scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
	url = f"{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
	resp = requests.get(url)
	return HttpResponse(resp.text)
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
