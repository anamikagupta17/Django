from django.shortcuts import render
from .froms import SignUpForm
from django.contrib import messages

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
    
