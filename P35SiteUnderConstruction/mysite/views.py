from django.shortcuts import render

# Create your views here.

def home(req):
    print("I am Home")
    return render(req,'home.html')

def about(req):
     print("I am About")
     return render(req,'about.html')
 
 


    
# this project is for: if you fixing some bugs and you don't want to show user so you
# can create middleware to show site in under construction   .if bug fixing done then just comment middleware call in settings .py
  
