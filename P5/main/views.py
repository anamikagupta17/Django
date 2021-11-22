from django import http
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html',{'url':'/contact'})  # we can not use this url in main .html becuse for that there is no view means no function
