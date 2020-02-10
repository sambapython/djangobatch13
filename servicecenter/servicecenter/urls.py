"""servicecenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from center.views import home_view, signout_view,signin_view, signup_view, googlesignin, googleauth, customer_view
from center.company import company_view_update, company_create_view, company_view_delete, CompanyListView
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView
from center.product import ProductTemplateView, productlist, ProductCreateView
from center.models import Product
from django.contrib.auth.decorators import login_required
from center.oauth import googleauth,googlelogin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',home_view),
    path("signout/",signout_view),
    path("signin/",signin_view),
    path("signup/",signup_view),
    path("company/",login_required(CompanyListView.as_view())),
    path("company_create/",company_create_view),
    re_path("company_update/(?P<pk>[0-9]+)",company_view_update),# company_view_update(req_obj,pk=2)
    re_path("company_delete/(?P<pk>[0-9]+)",company_view_delete),
    #path("product/",ProductTemplateView.as_view(template_name="center/product.html")),
    # path("product/",ListView.as_view(
    #     model = Product
    #     )),
    path("product/",productlist),
    path("product_create",login_required(ProductCreateView.as_view(
        # model=Product,
        # fields=['name',"description","company"],
        # success_url="/product",
        #template_name="center/productform.html",
        ))),
    re_path("product_update/(?P<pk>[0-9]+)/",login_required(UpdateView.as_view(
        model=Product,
        fields="__all__",
        success_url="/product",
        #template_name="center/productform.html",
        ))),
    re_path("product_delete/(?P<pk>[0-9]+)/",login_required(DeleteView.as_view(
        model=Product,
        success_url="/product",
        #template_name="center/productform.html",
        ))),
    path("api/",include("api.urls")),
    path("google/",googlelogin),
    path("auth/",googleauth),
    path("customer/",customer_view)


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns = urlpatterns+
#urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
