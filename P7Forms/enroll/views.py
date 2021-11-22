from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showFormData(request):
    # auto_id=False False will not create id and remove label tag or auto_id='txt' # its like true or 'id_%s'
    fm=StudentRegistration(auto_id='txt%s',label_suffix='  ',initial={'name':'Anamika Gupt','email':'anamika@gmail.com'})  #  it will remove : fro label , can given anything
    fm.order_fields(field_order=['first_name','name','password','email'])
    return render(request,'studentregistration.html',{'form':fm})
