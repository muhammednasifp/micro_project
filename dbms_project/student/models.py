from django.db import models
from django.contrib.auth.models import User
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="student",null=True)
    name=models.CharField(max_length=200)
    profile_image=models.ImageField(upload_to='profile_images/',null=True)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=200)
    dob = models.DateField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return self.name

class AcademicDetails(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="academic_details")
    year_sem = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    graduation = models.CharField(max_length=50)
    grade12 = models.DecimalField(max_digits=5, decimal_places=2)
    grade10 = models.DecimalField(max_digits=5, decimal_places=2)

   


class PlacementPreferences(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="placement_preferences")
    domain = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="skills")