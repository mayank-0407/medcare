from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import math
import random

# Create your views here.
def temp(request):
    return render(request,"home/temp.html")

def vhome(request):
    if request.user.is_superuser:
        return redirect('admin')

    if request.user.is_staff:
        return redirect('staffdashboard')  

    if request.user.is_active:
        return redirect('dashboard')

    return render(request,"home/home.html")

def dashboard(request):
    if request.user.is_authenticated:
        allmed=Medicine.objects.all()
        return render(request,"home/dashboard.html",context={'med':allmed})
    return redirect('home')

def my_admin(request):
    url=settings.BASE_URL_EMAIL+"/admin"
    response=redirect(url)
    return response

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        temp_email= request.POST.get('email')
        pass1= request.POST.get('password')

        email=temp_email.lower()
        try:
            verify_user=User.objects.get(username=email)    
        except:
            try:
                verify_user=User.objects.get(email=email)    
            except:
                messages.error(request, 'Error - The Entered Email is Not in our Records.')
                return redirect('signin') 
        try:
            tempuser=User.objects.get(email=email).username                  
            user=authenticate(request,username=tempuser,password=pass1)
            print(user)
        except:
            try:
                User.objects.get(username=email)
                
                user=authenticate(request,username=email,password=pass1)
            except:    
                messages.error(request, 'Error - The password you enetered is not associated with this email.')
                return redirect('signin')
        
        # print(user)            
        if user == None: 
            messages.error(request, 'Error - No User Exists.')
            return redirect('signin')
        if user.is_active == True:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Error - You dont have permission to login.')
            return redirect('signin')


    return render(request,"home/signin.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        name= request.POST.get('name')
        temp_email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('cpassword')
        city= request.POST.get('city')

        email=temp_email.lower()
        username=email

        if not pass1==pass2:
            messages.error(request, 'Error - Entered Passwords are same.')
            return redirect('signup')
        
        try:
            User.objects.get(email=email)
            messages.error(request, 'Error - Email Already exists.')
            return redirect('signup')
        except:
            pass

        myuser=User.objects.create_user(username=username,email=email,first_name=name)
        myuser.set_password(pass1)
        myuser.save()

        try:
            Customer.objects.create(user=myuser,
                                    city=city)
        except Exception as e:
            User.objects.get(id=myuser.id).delete()
            return HttpResponse(str(e))
        messages.error(request, 'Success - Verification link has been sent to your email. So Check You email and verify You email within 3 min otherwise link will expire')
        return redirect('home')

    return render(request,"home/signup.html")

def signout(request):
    logout(request)
    return redirect('home')

def viewmed(request):
    if request.user.is_authenticated:
        return render(request,"home/add_med.html")
    return redirect('home')

def addmedicine(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            name= request.POST.get('medicine_name')
            exp_date= request.POST.get('medicine_expire')
            price= request.POST.get('medicine_price')
            quantity= request.POST.get('medicine_quantity')
            description= request.POST.get('medicine_description')
            med_type= request.POST.get('medicine_type')

            try:
                mycustomer=Customer.objects.get(user=request.user)
                mytype=MedType.objects.get(code=med_type)
                med=Medicine.objects.create(mycustomer=mycustomer,
                                            name=name,
                                            expire_date=exp_date,
                                            price=price,
                                            quantity=quantity,
                                            description=description,
                                            type=mytype)
                print('added')
                messages.success(request,'Successfully Added Medcinine')
                med.save()
            except:
                messages.error(request, 'Error - Something went wrong.')
        return render(request,"home/dashboard.html")
    return redirect('home')