from django.shortcuts import render, redirect
from .models import Student, AcademicDetails, PlacementPreferences, Skill
# Create your views here.
def show_home(request):
    return render(request,'home.html')

def show_profile(request,student_id):
    student = Student.objects.select_related('academic_details', 'placement_preferences') \
                             .prefetch_related('skills') \
                             .get(id=student_id)

    context = {
        'student': student,
        'academic': getattr(student, 'academic_details', None),
        'placement': getattr(student, 'placement_preferences', None),
        'skills': student.skills.all(),  
    }
    # 'student' is the key for the Student object; used in the template as {{ student }}  
    # 'academic' fetches the student's AcademicDetails; getattr ensures it returns None if not set  
    # 'placement' fetches the student's PlacementPreferences; getattr ensures it returns None if not set  
    # 'skills' fetches all Skill objects linked to the student via ManyToManyField; returns a QuerySet  
    # context dictionary passes all this data from the view to the template so HTML can display it safely 
    return render(request, 'student_profile.html',context)

def registration(request):
    if request.method == "POST":
        #  Student Data 
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        dob = request.POST.get('dob')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')
        portfolio = request.POST.get('portfolio')

        #  Academic Details 
        yearsem = request.POST.get('yearsem')
        cgpa = request.POST.get('cgpa')
        graduation = request.POST.get('graduation')
        grade12 = request.POST.get('grade12')
        grade10 = request.POST.get('grade10')

        #  Placement Preferences 
        domain = request.POST.get('domain')
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        #  Skills 
        skill_names = request.POST.getlist('skill')  # multiple skills from checkboxes

        #  Create Student first 
        student_obj = Student(
            user=request.user, 
            name=name, email=email, phone=phone_number, dob=dob,
            linkedin=linkedin, github=github, portfolio=portfolio
        )
        student_obj.save()

        #  Create AcademicDetails 
        academic_obj = AcademicDetails(
            student=student_obj, year_sem=yearsem, cgpa=cgpa,
            graduation=graduation, grade12=grade12, grade10=grade10
        )
        academic_obj.save()

        #  Create PlacementPreferences 
        placement_obj = PlacementPreferences(
            student=student_obj, domain=domain, role=role,
            salary=salary, location=location
        )
        placement_obj.save()

        #  Create/Link Skills 
        skill_names = request.POST.getlist('skill')  # get all skills from form
        for name in skill_names:
            skill_obj, created = Skill.objects.get_or_create(name=name)
            student_obj.skills.add(skill_obj)  # link skill to student

        return redirect('home')  

    return render(request, 'registration.html')