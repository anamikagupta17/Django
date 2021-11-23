from django.shortcuts import render
from .forms import User
# Create your views here.
def user(request):
    fm=User()
    return render(request,'user.html',{'form':fm})


