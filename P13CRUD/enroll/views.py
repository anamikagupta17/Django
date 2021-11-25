from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
# Create your views here.

def showFormData(request):
    stuAll=Student.objects.all()
    print(stuAll)
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            data=fm.cleaned_data
            stu=Student(stuname=data['name'],stuemail=data['email'],stupass=data['password']) #for updating data add id=2
            stu.save()  #used for update and insert both when you give id then it will update
            
            # stu=Student(id=5) 
            # stu.delete() 
            return render(request,'success.html',{'form':fm})
           
    else:
        fm=StudentRegistration() 
        
    return render(request,'studentregistration.html',{'form':fm,'stu':stuAll})
