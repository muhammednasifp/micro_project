from django.shortcuts import render
from django.http import  HttpResponse

def trainer_homepage(request):
    return HttpResponse("Hello World")

def pending_page(request):
    print(request)
    return render(request,'trainer/pending_page.html')

def approved_page(request):
    print(request)
    return render(request,'trainer/approved_page.html')
