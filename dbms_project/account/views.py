from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db import transaction
from .models import UserType

def signout(request):
    logout(request)
    return redirect('home') 

def signin(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        user_type=UserType.objects.get(user=user)

        if user:
            login(request,user)
            if user_type.usertype == "student":
                return redirect('home')
            
            elif user_type.usertype == "trainer" and not user_type.is_approved:
                return redirect('pending_page')
            
            else:
                return redirect('approved_page')
        else:
            print('ERROR')
    return render(request,'UserLogin/signin.html')

@transaction.atomic
def signup(request):
    if request.method == "POST":
        try:
                username = request.POST['username']
                password = request.POST['password']
                usertype  = request.POST['userType']

                # username already exists
                if User.objects.filter(username=username).exists():
                    print("Username already exists")
                    return redirect('signup')

                user = User.objects.create_user(
                    username=username,
                    password=password,
                    
                )

                UserType.objects.create(
                    user=user,
                    usertype=usertype,
                    is_approved=False if usertype == "trainer" else True
                )

                if usertype == "trainer":
                    return redirect('pending_page')
                else:
                    return redirect('home')

        except Exception as e:
            print("Something went wrong. Try again.")
            print(e)

    return render(request, 'UserLogin/signup.html')
 