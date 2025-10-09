from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
from .models import Account
from django.contrib.auth import authenticate,login,logout

def signout(request):
    logout(request)
    return redirect('home') 

def signin(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')
           
        else:
            print('ERROR')
    return render(request,'signin.html')

def signup(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        account_obj=Account(name=username,email=email,password=password)
        account_obj.save()
        print('hello world')
        user=User.objects.create_user(username=username,password=password)
        if user:
          return  redirect('registration')
    
    return render(request,'signup.html')