from django.shortcuts import render,HttpResponseRedirect
from  .forms import Student
from .models import User
# Create your views here.
def home(req):
    if req.method =='POST':
        fm=Student(req.POST)
        if fm.is_valid():
            data=fm.cleaned_data
            reg=User(name=data['name'],email=data['email'],password=data['password'])
            reg.save()
            fm=Student() 
        
    else:
       fm=Student() 
       
    stu=User.objects.all()
    return render(req,'addShow.html',{'fm':fm,'stu':stu})

def deleteData(req,id):
    if req.method =='POST':   # we can do this with get method also
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def editData(req,id) :
    if req.method =='POST':
       pi=User.objects.get(pk=id)
       fm=Student(req.POST,instance=pi) #for particular data
       if fm.is_valid():
           fm.save()    #we can updtae specific fields also like add
           return HttpResponseRedirect('/')    
    else :
      pi=User.objects.get(pk=id)
      fm=Student(instance=pi)     
        
    return render(req,'update.html',{'fm':fm})   
    
    

