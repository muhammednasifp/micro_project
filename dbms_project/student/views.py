from django.shortcuts import render, redirect
from .models import Student, AcademicDetails, PlacementPreferences, Skill
from django.http import HttpResponse
 
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

def registration(request, student_id=None):

    # ------------------ Fetch existing if editing ------------------
    student_obj = None
    academic_obj = None
    placement_obj = None

    if student_id:   # Edit Mode
        student_obj = Student.objects.filter(id=student_id).first()  # No error
    if student_obj:
        academic_obj = AcademicDetails.objects.filter(student=student_obj).first()
        placement_obj = PlacementPreferences.objects.filter(student=student_obj).first()

    # ------------------ POST Request ------------------
    if request.method == "POST":

        # Student Data
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        dob = request.POST.get('dob')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')
        portfolio = request.POST.get('portfolio')

        # Academic Data
        yearsem = request.POST.get('yearsem')
        cgpa = request.POST.get('cgpa')
        graduation = request.POST.get('graduation')
        grade12 = request.POST.get('grade12')
        grade10 = request.POST.get('grade10')

        # Placement Data
        domain = request.POST.get('domain')
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        # Skills
        skill_names = request.POST.getlist('skill')

        # ------------------ CREATE or UPDATE Student ------------------
        if student_obj:  # Update mode
            student_obj.name = name
            student_obj.email = email
            student_obj.phone = phone_number
            student_obj.dob = dob
            student_obj.linkedin = linkedin
            student_obj.github = github
            student_obj.portfolio = portfolio
            student_obj.save()
        else:  # Create mode
            student_obj = Student.objects.create(
                user=request.user,
                name=name, email=email, phone=phone_number, dob=dob,
                linkedin=linkedin, github=github, portfolio=portfolio
            )

        # ------------------ Academic ------------------
        if academic_obj:
            academic_obj.year_sem = yearsem
            academic_obj.cgpa = cgpa
            academic_obj.graduation = graduation
            academic_obj.grade12 = grade12
            academic_obj.grade10 = grade10
            academic_obj.save()
        else:
            academic_obj = AcademicDetails.objects.create(
                student=student_obj, year_sem=yearsem, cgpa=cgpa,
                graduation=graduation, grade12=grade12, grade10=grade10
            )

        # ------------------ Placement ------------------
        if placement_obj:
            placement_obj.domain = domain
            placement_obj.role = role
            placement_obj.salary = salary
            placement_obj.location = location
            placement_obj.save()
        else:
            placement_obj = PlacementPreferences.objects.create(
                student=student_obj, domain=domain, role=role,
                salary=salary, location=location
            )

        # ------------------ Skills ------------------
        student_obj.skills.clear()  # Remove old skills
        for name in skill_names:
            skill_obj, created = Skill.objects.get_or_create(name=name)
            student_obj.skills.add(skill_obj)

        return redirect('student_profile', student_id=student_obj.id)

    # ------------------ GET Request: Load form ------------------
    context = {
        "student": student_obj,
        "academic": academic_obj,
        "placement": placement_obj,
        "skills": student_obj.skills.all() if student_obj else [],
        "is_edit": True if student_id else False
    }

    return render(request, 'registration.html', context)
