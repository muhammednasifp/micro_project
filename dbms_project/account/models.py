from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    USER_TYPES = [
        ('trainer', 'Trainer'),
        ('student', 'Student'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=20, choices=USER_TYPES)
    is_approved = models.BooleanField(default=False)

    def __str__(self)->str:
        return self.user.username