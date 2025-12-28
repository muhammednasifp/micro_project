from django.shortcuts import render
from  .models import Placement_details,PlacementPreferences


def show_placement(request):
    
    pref_obj=PlacementPreferences.objects.all()

    placement_obj=Placement_details.objects.all()

    context={
            'placements': placement_obj
    }

    return render(request,'placement.html',context)