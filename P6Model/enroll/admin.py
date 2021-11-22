from django.contrib import admin
from enroll.models import Student
#admin.site.register(Student)  # for showing table data in admin panel

# Register your models here.
@admin.register(Student)  #decorater for loading multiple classes
class StudentAdmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail','stupass')


#admin.site.register(Student,StudentAdmin)