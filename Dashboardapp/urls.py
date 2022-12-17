from django.urls import path
from . import views

app_name = "Dashboardapp"    #testing

urlpatterns = [
    path('',views.VCpage,name='VCPage'),
]