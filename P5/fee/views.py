from django.shortcuts import render

# Create your views here.

def fees(request):
    return render(request ,'fee.html')
