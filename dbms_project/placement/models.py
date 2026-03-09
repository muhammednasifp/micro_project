from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255,null=True)
    company_logo = models.ImageField(upload_to='company_logos/',null=True)  
    company_url=models.CharField(max_length=255,null=True)

class Placement(models.Model):

    EMPLOYMENT_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('internship', 'Internship'),
        ('part-time', 'Part-time'),
    ]

    WORK_MODE_CHOICES = [
        ('on-site', 'On-site'),
        ('remote', 'Remote'), 
        ('hybrid', 'Hybrid'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default="full-time",null=True)
    work_mode = models.CharField(max_length=20, choices=WORK_MODE_CHOICES, default="on-site",null=True)
    job_title = models.CharField(max_length=255,null=True)
    domain = models.CharField(max_length=200,null=True)
    package = models.CharField(max_length=50,null=True)  # "₹12 LPA"
    location = models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=20,null=True)
    vacancy_no=models.IntegerField(null=True)
    min_gpa=models.CharField(max_length=20,null=True)
    passing_year=models.CharField(max_length=30,null=True)

class JobDetails(models.Model):
    
    placement = models.OneToOneField(Placement, on_delete=models.CASCADE)
    job_description=models.TextField(blank=True)
    responsibilities=models.TextField(blank=True)
    required_skills=models.TextField(blank=True)

    
