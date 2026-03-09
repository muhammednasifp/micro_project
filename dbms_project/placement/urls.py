
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('placement',views.show_placement,name='placement'),
    path('placement_details<int:placement_id>',views.placement_details,name='details')
]
