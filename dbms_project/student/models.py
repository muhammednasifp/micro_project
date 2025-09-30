from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=200)
    dob = models.DateField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return str.name

class AcademicDetails(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="academic_details")
    course = models.CharField(max_length=100)
    year_sem = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    graduation = models.CharField(max_length=50)
    grade12 = models.DecimalField(max_digits=5, decimal_places=2)
    grade10 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self)->str:
        return str.name


class PlacementPreferences(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="placement_preferences")
    domain = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    def __str__(self)->str:
        return str.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="skills")