from django.shortcuts import render
from .forms import Login

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    fm=Login()
    return render(request,'login.html',{'form':fm})