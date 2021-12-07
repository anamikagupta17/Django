from django.shortcuts import render
# Create your views here.
def home(req):
    return render(req,'home.html')

def show(request,id=1):
    return render(request,'show.html',{'id':id})

