from django.db import models

# Create your models here.

class Account(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=10)

    def __str__(self)->str:
        return self.name