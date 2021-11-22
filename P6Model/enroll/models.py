from typing_extensions import Concatenate
from django.db import models

# Create your models here.

class Student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=70)
    stuemail=models.CharField(max_length=70)
    stupass=models.CharField(max_length=40)
    comment=models.TextField(max_length=40,default='Not Available')
    
    def __str__(self):  # if we wanted to show only a single column  if we give id then need to convert that into string
        return self.stuname+" "+self.stuemail