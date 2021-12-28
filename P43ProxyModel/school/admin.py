from django.contrib import admin
from .models import ExamCenter,MyProxyExamCenter

# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']



@admin.register(MyProxyExamCenter)
class MyProxyExamCenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']
    
