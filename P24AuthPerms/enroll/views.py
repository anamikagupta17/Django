from django.shortcuts import render
from .froms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
# Create your views here.

#create users
def signup(req):
    if req.method=='POST':
        fm=SignUpForm(req.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='editor')
            user.groups.add(group)
            messages.success(req,'User Added Successfully')
            fm=SignUpForm()
            
    else:        
      fm=SignUpForm()
      
    return render (req,'signup.html',{'fm':fm})
  
  
def userLogin(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      fm=AuthenticationForm(request=request,data=request.POST)
      if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass) # authenticate from db means match username and password from db
            print(user)
            if user is not None:
              login(request, user)
              messages.success(request,'Login Successfully')
              return HttpResponseRedirect('/dashboard/')
    else:
      fm=AuthenticationForm()
    return render (request,'login.html',{'form':fm})
  else:
    return HttpResponseRedirect('/dashboard/')


def dashboard(req):
  if req.user.is_authenticated: 
    
    return render (req,'dashboard.html',{'name':req.user.username})
    
  else :
     return HttpResponseRedirect('/login/')

def userLogout(req):
  logout(req)
  return HttpResponseRedirect('/login/')

   
   
  
    
