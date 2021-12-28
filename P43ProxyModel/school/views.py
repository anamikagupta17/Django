from django.shortcuts import render
from .models import ExamCenter,MyProxyExamCenter

# Create your views here.

def home(req):
    centers=ExamCenter.objects.all()
    proxycenters=MyProxyExamCenter.objects.all()
    return render(req,'home.html',{'centers':centers,'proxycenters':proxycenters})
    
