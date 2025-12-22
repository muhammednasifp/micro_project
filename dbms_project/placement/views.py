from django.shortcuts import render
from  .models import Placement_details


def show_placement(request):

    placement_obj=Placement_details.objects.all()

    context={
            'placements': placement_obj
    }

    return render(request,'placement.html',context)