from django.shortcuts import render,HttpResponse
from blog import signals

# Create your views here.
def home(req):
    signals.nofitifaction.send(sender=None,request=req,user=['Anamika','Gupta'])
    return HttpResponse('This is home page')
    
