from django.shortcuts import render
from center.models import RequestTracker
class RequestTrackerMiddleware:
	def __init__(self, view):
		self.view = view 

	def __call__(self,request):
		print("before calling the view")
		reqt = RequestTracker(request_url=request.META.get('PATH_INFO'),client_ip=request.META.get('USERDOMAIN'))
		resp = self.view(request) # to execute the view
		status_code = resp.status_code
		reqt.resp_code = status_code
		reqt.save()
		if status_code==404:
			return render(request, "center/404.html")
		print("before sending the response")
		return resp