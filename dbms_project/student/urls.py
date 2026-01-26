
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_home,name='home'),
    path('profile<int:student_id>/',views.show_profile,name='student_profile'),
    path('registration/<int:student_id>/',views.registration,name='student_registration'),
]
