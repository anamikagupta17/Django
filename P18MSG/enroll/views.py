from django.shortcuts import render,HttpResponseRedirect
from  .forms import Student
from .models import User
from django.contrib import messages
# Create your views here.
def home(req):
    if req.method =='POST':
        fm=Student(req.POST)
        if fm.is_valid():
            fm.save() 
            #messages
            messages.add_message(req,messages.SUCCESS,'Student Added Sucessfully!')
            print(messages.get_level(req))
            fm=Student() 
        
    else:
       fm=Student() 
       
    stu=User.objects.all()
    return render(req,'addShow.html',{'fm':fm,'stu':stu})

def deleteData(req,id):
    if req.method =='POST':   # we can do this with get method also
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.warning(req,'Deleted Sucessfully')
        return HttpResponseRedirect('/')
    
def editData(req,id) :
    if req.method =='POST':
       pi=User.objects.get(pk=id)
       fm=Student(req.POST,instance=pi) #for particular data
       if fm.is_valid():
           fm.save()    #we can updtae specific fields also like add
           messages.add_message(req,messages.INFO,'Updated Sucessfully!')
           messages.success(req,'Keep Going')  # we can write both types
           return HttpResponseRedirect('/')    
    else :
      pi=User.objects.get(pk=id)
      fm=Student(instance=pi)     
        
    return render(req,'update.html',{'fm':fm})   

def msg(req):
    messages.debug(req,'This is Debug')# this will not display untill you won't set it by set_level
    messages.set_level(req,messages.DEBUG)
    messages.debug(req,'This is  new Debug ') 
    messages.info(req,'This is Info')
    messages.success(req,'This is Success')
    messages.warning(req,'This is Warning')
    messages.error(req,'This is Error')
    return render(req,'messages.html')
    
    

