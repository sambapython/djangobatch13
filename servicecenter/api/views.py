from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from center.models import UserProfile
from api.serializers import UserCreateSerilizer, UserGetSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
class UserModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class=UserCreateSerilizer

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return UserGetSerializer
        return self.serializer_class


#APIView, viewsets.Viewset, viewsets.ModelViewset

# Create your views here.
# class UserAPIView(APIView):
#     def get(self, request):
#         l=["user1","user2","user3"]
#         return Response(l)
#     def post(self, request):

#         data = request.data 
#         ser = UserCreateSerilizer(data=data)
#         if ser.is_valid():
#             ser.save()
#             user = ser.instance
#             user.set_password(data.get("password"))
#             user.save()
#             ser = UserGetSerializer(data)
#             return Response({"message":"user created successfully",
#             "data":ser.data})
#         else:
#             return Response({"message":ser._errors,"data":{}}, status=status.HTTP_400_BAD_REQUEST)

#         #user = UserProfile(**data)
#         #user.save()
#         #user.set_password(data.get("password"))
#         #user.save()
        
#     def put(self, request, id):
#         return Response("put")
#     def delete(self,request, id):
#         return Response("delete")

