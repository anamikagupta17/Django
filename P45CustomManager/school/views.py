from django.shortcuts import render
from .models import Student

# Create your views here.
def home(req):
   
    # students=Student.objects.all() # if use custom manager then need to define in models
    #students=Student.custommanager.all() #custom manager associated in model.using predifne function
    
    students=Student.custommanager.get_stu_roll_range(102,105) # custom method
    
    return render(req,'home.html',{'students':students})
