from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,'My_app/index.html')

def other(request):
    return render (request,'My_app/other.html')

def relative(request):
    return render (request,'My_app/relative.html')