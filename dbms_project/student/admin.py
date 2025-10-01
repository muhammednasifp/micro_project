from django.contrib import admin
from .models import Student,AcademicDetails,PlacementPreferences,Skill
# Register your models here.
admin.site.register(Student)
admin.site.register(AcademicDetails)
admin.site.register(PlacementPreferences)
admin.site.register(Skill)