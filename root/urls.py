from django.contrib import admin
from django.urls import path , include
from .views import *
app_name = 'root'
urlpatterns = [
    path('admin/', admin.site.urls),
    path ("" , home , name="home"),
]