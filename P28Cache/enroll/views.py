from django.shortcuts import render
from django.views.decorators.cache import cache_page #only for view based cache

# Create your views here.

def home(request):
    return render(request,'course.html')

@cache_page(30)
def viewBased(request):
    return render(request,'viewbased.html')

def contact(request):
    return render(request,'contact.html')

def templateFragmentBased(request):
    return render(request,'templatefragment.html')
