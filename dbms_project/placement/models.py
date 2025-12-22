from django.db import models

# Create your models here.

class Placement_details(models.Model):
   
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

    company_name = models.CharField(max_length=255,null=True)
    company_logo = models.ImageField(upload_to='company_logos/',null=True)  
    job_title = models.CharField(max_length=255,null=True)
    domain = models.CharField(max_length=200,null=True)
    package = models.CharField(max_length=50,null=True)  # "₹12 LPA"
    location = models.CharField(max_length=100,null=True)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default="full-time",null=True)
    work_mode = models.CharField(max_length=20, choices=WORK_MODE_CHOICES, default="on-site",null=True)


    def __str__(self)->str:
        return self.company_name
