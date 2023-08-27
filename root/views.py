from django.shortcuts import render

def home(requset):
    return render (requset , 'root/index.html')

def about(requset):
    return render (requset , 'root/about.html')

def contact(requset):
    return render (requset , 'root/contact.html')
# Create your views here.
