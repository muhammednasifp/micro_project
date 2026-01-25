
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('placement<int:student_id>',views.show_placement,name='placement'),
    path('details',views.placement_details,name='details')
]
