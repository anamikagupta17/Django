from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','marks','pass_date','admit_date']
