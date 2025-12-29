from django.shortcuts import render,get_object_or_404
from  .models import Placement_details
from django.db.models import Q
from student.models import PlacementPreferences


def show_placement(request, student_id):
    
    pref = get_object_or_404(PlacementPreferences,student_id=student_id)

    domains = [d.strip() for d in pref.domain.split(',')]  # multiple domain support

    companies = Placement_details.objects.filter(
            Q(domain__icontains=pref.domain) |
            Q(job_title__icontains=pref.role) |
            Q(location__icontains=pref.location) |
            Q(package__icontains=pref.salary)
    )

    return render(request,"placement.html",{"placements":companies})
