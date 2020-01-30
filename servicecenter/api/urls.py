from django.urls import path, re_path, include
from django.http import HttpResponse
from api.views import UserAPIView
urlpatterns =[

    path("users/",UserAPIView.as_view()),
    re_path("users/(?P<id>[0-9]+)",UserAPIView.as_view())
]