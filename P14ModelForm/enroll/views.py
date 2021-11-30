from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
# Create your views here.
def home(req):
    return render(req,'home.html')

def showFormData(request):
    stuAll=Student.objects.all()
    print(stuAll)
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        # pi=Student.objects.get(pk=1)
        # fm=StudentRegistration(request.POST,instance=pi) #instance for update
        if fm.is_valid():
            data=fm.cleaned_data
            print('Name : ',data['name'])
            print('Password : ',data['password'])
            print('Email : ',data['email'])
            stu=Student(name=data['name'],email=data['email'],password=data['password'])
            stu.save()
            #update
            # stu=Student(id=4,name=data['name'],email=data['email'],password=data['password'])
            # stu.save()
            #delete
            # stu=Student(id=5)
            # stu.delete()
            #instance for update
           # fm.save()
            return render(request,'success.html',{'form':fm})
           
    else:
        fm=StudentRegistration() 
        
    return render(request,'studentregistration.html',{'form':fm,'stu':stuAll})
