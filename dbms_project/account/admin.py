from django.contrib import admin
from .models import UserType

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'usertype', 'is_approved')
    list_display_links = ('user',)
    list_filter = ('usertype', 'is_approved')
    list_editable = ('is_approved',)

  