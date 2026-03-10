from django.shortcuts import render,get_object_or_404
from  .models import Company,Placement,JobDetails
from django.db.models import Q
from student.models import PlacementPreferences,Student


def show_placement(request):
    student = Student.objects.select_related(
    'placement_preferences'
    ).get(user=request.user)

    pref= student.placement_preferences

    query = Q()

    if pref.domain:
        query &= Q(domain__icontains=pref.domain)

    if pref.location:
        query &= Q(location__icontains=pref.location)

    if pref.salary:
        query &= Q(package__gte=pref.salary)
    
    placements = Placement.objects.select_related("company").filter(query)

    return render(request,'placement/placement.html',{"placements":placements})

def placement_details(request,placement_id):
    return render(request,'placement/placement_details.html')
