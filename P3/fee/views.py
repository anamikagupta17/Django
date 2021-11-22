from django.shortcuts import render
from django.http import HttpResponse
def  fee_python(request):
    return HttpResponse("<h2>Learn Python Fee </h3>")
def fee_django(request):
    return HttpResponse("<h2>Learn Django Fee </h3>")    

# Create your views here.
