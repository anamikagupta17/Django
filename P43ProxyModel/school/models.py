from django.db import models
from django.db.models.fields import proxy

# Create your models here.

class ExamCenter(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    
    
class MyProxyExamCenter(ExamCenter):
    class Meta:
        proxy=True
        ordering=['city']  # this will change the order for display data 
        