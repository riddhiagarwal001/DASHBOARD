"""Dashboardproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from Dashboardapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.AdminPage),
    path('VCMASTER.html', include('Dashboardapp.urls',namespace="Dashboardapp")),
    path('VMASTER.html',views.Vpage,name="Vpage"),
    path('PARTMASTER.html',views.Partpage,name="Partpage"),
    path('STRLOC.html',views.StrPage,name="StrPage"),
    path('MAPMASTER.html',views.MapPage,name="MapPage"),
    path('MRP.html',views.mrpPage,name="mrpPage"),
    path('DML.html',views.dmlPage,name="dmlPage"),
    ]
