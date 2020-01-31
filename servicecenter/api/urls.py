from django.urls import path, re_path, include
from django.http import HttpResponse
#from api.views import UserAPIView
from api.views import UserModelViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('users', UserModelViewSet) 
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
 path('docs', schema_view),
]
urlpatterns = urlpatterns+router.urls

# urlpatterns =[

#     path("users/",UserAPIView.as_view()),
#     re_path("users/(?P<id>[0-9]+)",UserAPIView.as_view())
# ]