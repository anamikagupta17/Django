from django.shortcuts import render,HttpResponse
 

# Create your views here.

def home(req):
    print('I am View')
    return HttpResponse('This is view  Function Based Middleware......<br><br> <a href="/cls">Class Based</a>  ')
