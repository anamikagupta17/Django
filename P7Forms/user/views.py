from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import User
# Create your views here.
def user(request):
    if request.method=='POST':
        fm=User(request.POST)
        if fm.is_valid():
            print('From Validated')
            print('Name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email'])
           # return render(request,'success.html',{'nm':fm.cleaned_data['name']}) #url will not chnage becuse it will called in this fuction only
            return HttpResponseRedirect('/user/success') # this will call view according to the url
    else:   
        fm=User()
        
    return render(request,'user.html',{'form':fm})


def success(req):
    return render(req,'success.html')

def formFields(request):
    fmm=User()
    return render(request,'formFields.html',{'form':fmm})


