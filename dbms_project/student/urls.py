
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_home,name='home'),
    path('profile<int:student_id>',views.show_profile,name='student_profile'),
    path('editprofile<int:student_id>',views.edit_profile,name='edit_profile'),
    path('registration/',views.registration,name='student_registration'),
]
