from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from center.models import UserProfile

#APIView, viewsets.Viewset, viewsets.ModelViewset

# Create your views here.
class UserAPIView(APIView):
    def get(self, request):
        l=["user1","user2","user3"]
        return Response(l)
    def post(self, request):
        data = request.data 
        user = UserProfile(**data)
        user.save()
        user.set_password(data.get("password"))
        user.save()
        return Response({"message":"user created successfully",
        "data":{"username":user.username}})
    def put(self, request, id):
        return Response("put")
    def delete(self,request, id):
        return Response("delete")

