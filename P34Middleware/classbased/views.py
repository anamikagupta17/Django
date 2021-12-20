from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(req):
    print('I am View')
    return HttpResponse('This is view  Class Based Middleware ..... <br><br><a href="/multiple">Multiple</a> ')


def multiple(req):
    print('I am View')
    return HttpResponse('This is view  Multiple Middleware  ')


def excp(req):
    a=10/0
    return HttpResponse('This is exception View')


def user_info(req):
    print('I am user Info View')
    context={'name':'Anamika Gupta'}
    return TemplateResponse(req,'user_info.html',context)