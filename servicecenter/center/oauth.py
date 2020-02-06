
import os 
from django.conf import settings
from center.models import UserProfile
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import requests
from django.contrib.auth import login
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def create_or_get_add_session(request, username):
	user,created = UserProfile.objects.get_or_create(
		username=username)
	login(request, user)


def googlelogin(request):
	token_request_uri = "https://accounts.google.com/o/oauth2/auth"
	response_type = "code"
	scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
	url = f"{token_request_uri}?response_type={response_type}&client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.GOOGLE_REDIRECT_URL}&scope={scope}"
	print(url)
	#resp = requests.get(url)
	return HttpResponseRedirect(url)

def googleauth(request):
	code=request.GET.get('code')
	access_token_uri = 'https://accounts.google.com/o/oauth2/token'
	resp = requests.post(access_token_uri, json={
		'code':code,
		'redirect_uri':settings.GOOGLE_REDIRECT_URL,
		'client_id':settings.GOOGLE_CLIENT_ID,
		'client_secret':settings.GOOGLE_CLIENT_SECRET,
		'grant_type':'authorization_code'
	})
	token_data = resp.json().get("access_token")
	print("*"*100)
	print(token_data)
	resp = requests.get(f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={token_data}")
	user_data = resp.json()
	username = user_data.get("email")
	create_or_get_add_session(request, username)
	#we need to take the userinfo
	# add user details to the session
	return redirect("/")

def fblogin(request):
	authorization_base_url = 'https://www.facebook.com/dialog/oauth'
	
	facebook = OAuth2Session(fb_client_id, redirect_uri=fb_redirect_uri)
	facebook = facebook_compliance_fix(facebook)
	authorization_url, state = facebook.authorization_url(authorization_base_url)
	return HttpResponseRedirect(authorization_url)

def fbauth(request):
	redirect_response = request.GET.get("code")
	facebook = OAuth2Session(fb_client_id, redirect_uri=fb_redirect_uri)
	facebook = facebook_compliance_fix(facebook)
	token_url = 'https://graph.facebook.com/oauth/access_token'
	token = facebook.fetch_token(token_url, client_secret=fb_client_secret,
                      code=redirect_response)
	print("*" * 100)
	access_token = token.get("access_token")
	resp = requests.get('https://graph.facebook.com/me?access_token=%s'%access_token)
	return HttpResponse(resp.content)