from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html', {'home':'active'})

def contact(request):
    return render(request,'contact.html',{'contact':'active'})