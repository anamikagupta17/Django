from django.contrib import admin
from .models import Student,Teacher,Construction

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fees']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date']



@admin.register(Construction)
class ConstructionAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','payment']
