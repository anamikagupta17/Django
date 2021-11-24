from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showFormData(request):
    
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            data=fm.cleaned_data
            print('Name : ',data['name'])
            print('Email : ',data['email'])
            print('Password : ',data['password'])
            print('Confirm Password : ',data['confirm_password'])
    else:
        fm=StudentRegistration() 
    return render(request,'studentregistration.html',{'form':fm})
