from django.shortcuts import render

# Create your views here.
def show_placement(request):
    return render(request,'placement.html')