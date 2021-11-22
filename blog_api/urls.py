"""blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


# Create your views here.
def home_view(request, *args, **kwargs):

    html_doc = """
    <center><h1>Django REST api </h1> <br/><br/>
    <a href='./vlog/api' > VLOGS APP </a> <br/><br/>
    <a href='./blog/api' > The Blog </a> <br/>
    """
    return HttpResponse(html_doc)


urlpatterns = [
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("blog/api/", include("blog.urls")),
    path("vlog/api/", include("vlogs.urls")),
]


urlpatterns = format_suffix_patterns(urlpatterns)
