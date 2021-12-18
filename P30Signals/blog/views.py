from django.shortcuts import render

# Create your views here.

def home(request):
    a=10
    b=0
    c=a/b
    print(c)