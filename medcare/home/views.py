from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def vhome(request):
    return render(request,"home/home.html")