
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('placement/',views.show_placement,name='placement')
]
