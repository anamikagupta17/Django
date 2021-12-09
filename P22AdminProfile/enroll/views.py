from django.shortcuts import render
from .froms import SignUpForm,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.http import HttpResponseRedirect
# Create your views here.

def signup(req):
    if req.method=='POST':
        fm=SignUpForm(req.POST)
        if fm.is_valid():
            fm.save()
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
              return HttpResponseRedirect('/profile/')
    else:
      fm=AuthenticationForm()
    return render (request,'login.html',{'form':fm})
  else:
    return HttpResponseRedirect('/profile/')


def profile(req):
  if req.user.is_authenticated: 
     if req.method == 'POST':
      fm=EditUserProfileForm(req.POST,instance=req.user)
      if fm.is_valid():
        fm.save()
        messages.success(req,"Profile Updated Successfully!")
        return HttpResponseRedirect('/profile/')
     else: 
       fm=EditUserProfileForm(instance=req.user)
     return render(req,'profile.html',{'name':req.user,'form':fm})
  else :
     return HttpResponseRedirect('/login/')

def userLogout(req):
  logout(req)
  return HttpResponseRedirect('/login/')

def changepas(req):
  if req.user.is_authenticated: 
    if req.method == 'POST':
      fm=PasswordChangeForm(user=req.user,data=req.POST)
      if fm.is_valid():
        fm.save()
        update_session_auth_hash(req,fm.user) # otherwise it will logout automatically because seesion expired.this will keep session update or active 
        messages.success(req,'Password Changed Successsfully!')
        return HttpResponseRedirect('/profile/')
    else:
      fm=PasswordChangeForm(user=req.user)
    return render(req,'changepas.html',{'form':fm})
  else :
     return HttpResponseRedirect('/login/')
  
    
