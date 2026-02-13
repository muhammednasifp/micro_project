from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CompanyForm, PlacementForm, JobDetailsForm

def trainer_dashboard(request):

    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES)
        placement_form = PlacementForm(request.POST)
        job_form = JobDetailsForm(request.POST)

        if company_form.is_valid() and placement_form.is_valid() and job_form.is_valid():

            # Save Company
            company = company_form.save()

            # Save Placement but attach company
            placement = placement_form.save(commit=False)
            placement.company = company
            placement.save()

            # Save Job Details
            job_details = job_form.save(commit=False)
            job_details.placement = placement
            job_details.save()

            return redirect('trainer_dashboard')

    else:
        company_form = CompanyForm()
        placement_form = PlacementForm()
        job_form = JobDetailsForm()

    return render(request, 'trainer/trainer_home.html', {
        'company_form': company_form,
        'placement_form': placement_form,
        'job_form': job_form,
    })


def pending_page(request):
    
    return render(request,'trainer/pending_page.html')
