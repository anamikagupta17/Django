from django.shortcuts import render
from django.http import HttpResponse
def  learn_python(request):
    return HttpResponse("<h2>Learn Python </h3>")
def learn_django(request):
    return HttpResponse("<h2>Learn Django </h3>")    

# Create your views here.
