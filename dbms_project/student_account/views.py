from django.shortcuts import render
from django.contrib.auth.models  import User
from .models import Account
# Create your views here.

def signin(request):

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
    
    return render(request,'signup.html')