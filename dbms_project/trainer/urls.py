
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('pending_page/',views.pending_page,name='pending_page'),
    path('trainer_dashboard',views.trainer_dashboard,name='trainer_dashboard')
]
