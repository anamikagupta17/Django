from datetime import datetime, timedelta
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def setcookie(request):
    response= render(request,'setcookie.html')
    response.set_cookie('name','Parul',expires=datetime.utcnow()+timedelta(days=2)) #max_age=50 in sec
    return response


def getcookie(request):
   # name=request.COOKIES['name']  #method 1 value not there then will return eerror
   # name=request.COOKIES.get('name','Guest') #method 2     value not there then will return None
    name=request.COOKIES.get('name','Guest') #here we can set default
    return render(request,'getcookie.html',{'name':name})


def delcookie(request):
    response= render(request,'delcookie.html')
    response.delete_cookie('name')
    return response


def setsigned(request):
    response= render(request,'setcookie.html')
    response.set_signed_cookie('name','Anamika',salt='nm',expires=datetime.utcnow()+timedelta(days=2)) #max_age=50 in sec
    return response


#can only acces when we have salt name
def getsignedcookie(request):
    name=request.get_signed_cookie('name',default='Default Value',salt='nm') #salt name should be same as we given at the time of setcookie
    return render(request,'getcookie.html',{'name':name})

