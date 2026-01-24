from django.urls import path
from .views import placement_list,student_list,academic_list,skill_list,preferences_list

urlpatterns = [
    path('placement_api/',view=placement_list,name='placement_api'),
    path('student_api/',view=student_list,name='student_api'),
    path('skill_api/',view=skill_list,name='skill_api'),
    path('academic_api/',view=academic_list,name='academic_api'),
    path('pref_api/',view=preferences_list,name='pref_api')
]
