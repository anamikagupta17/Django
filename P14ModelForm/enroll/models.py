from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=70,blank=True) # blank it will make required False
    email=models.CharField(max_length=70)
    password=models.EmailField(max_length=40)
