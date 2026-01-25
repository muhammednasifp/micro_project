from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
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
    return render(request,'UserLogin/signin.html')

def signup(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        if user:
          return  redirect('home')
    
    return render(request,'UserLogin/signup.html')