from django.contrib import admin
from .models import Company,Placement,JobDetails
# Register your models here.
admin.site.register(Company)
admin.site.register(Placement)
admin.site.register(JobDetails)
