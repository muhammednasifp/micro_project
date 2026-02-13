from django.shortcuts import render,get_object_or_404
from  .models import Company,Placement,JobDetails
from django.db.models import Q
from student.models import PlacementPreferences


def show_placement(request, student_id):
    
    pref = get_object_or_404(PlacementPreferences,student_id=student_id)
    
    return render(request,"placement/placement.html",)

def placement_details(request,placement_id):

    return render(request,'Placement/placement_details.html')
