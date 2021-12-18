from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponseRedirect
from blog.froms import SignupForm,LoginFrom,PostForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Post

# Create your views here.

def home(req):
    posts=Post.objects.all()
    return render(req,'home.html',{'posts':posts})

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def dashboard(req):
    if  req.user.is_authenticated:
        posts=Post.objects.all()
        user=req.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        ip=req.session.get('ip',0)
        return render(req,'dashboard.html',{'posts':posts,'name':full_name,'groups':gps,'ip':ip})
    else:
        return HttpResponseRedirect('/login/')
    

def signup(req):
    if req.method=='POST':
        fm=SignupForm(req.POST)
        if fm.is_valid():
           user= fm.save()
           group=Group.objects.get(name='Author')
           user.groups.add(group)
           messages.success(req,'Congratulations!! You became  an Author')
           return HttpResponseRedirect('/signup/')
    else:
       fm=SignupForm()
    return render(req,'signup.html',{'form':fm})

def userlogin(req):
    if not req.user.is_authenticated:
        if req.method=='POST':
            fm=LoginFrom(request=req ,data=req.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(req,user)
                    messages.success(req,'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=LoginFrom()
        return render(req,'login.html',{'form':fm})
    else :
        return HttpResponseRedirect('/dashboard/')   

def userlogout(req):
    logout(req)
    return HttpResponseRedirect('/')

def addpost(req):
    if  req.user.is_authenticated:
        if req.method == 'POST':
            fm=PostForm(req.POST)  
            if fm.is_valid():
                fm.save()
                messages.success(req,'Post Added Successfully')
                return HttpResponseRedirect('/dashboard/') 
           
        else:
            fm=PostForm()      
        return render(req,'addpost.html',{'form':fm})
    else:
       return HttpResponseRedirect('/login/')
   
def updatepost(req,id):
    if  req.user.is_authenticated:
        if req.method == 'POST':
            pi=Post.objects.get(pk=id)
            fm=PostForm(req.POST,instance=pi)  
            if fm.is_valid():
                fm.save()
                messages.success(req,'Post Updated Successfully')
                return HttpResponseRedirect('/dashboard/') 
        else:
            pi=Post.objects.get(pk=id)
            fm=PostForm(instance=pi)
        return render(req,'updatePost.html',{'form':fm})
    else:
       return HttpResponseRedirect('/login/')   
   
def deletepost(req,id):
    if  req.user.is_authenticated:
        if req.method == 'POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            messages.success(req,'Post Deleted Successfully')
            return HttpResponseRedirect('/dashboard/') 
    else:
       return HttpResponseRedirect('/login/')     