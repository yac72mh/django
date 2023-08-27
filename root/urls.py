from django.urls import path , include
from .views import *


app_name = 'root'
urlpatterns = [
    path ("" , home , name="home"),
    path ("about" , about , name="about"),
    path ("contact" , contact , name="contact"),
]
