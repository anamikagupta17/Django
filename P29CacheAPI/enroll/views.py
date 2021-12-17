from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

# def home(request):
#     # mv=cache.get('movie','has_expired')
#     # if mv=='has_expired':
#     #     cache.set('movie','Anamika',30)
#     #     mv=cache.get('movie')
#   #or
#    # mv=cache.get_or_set('fees',5000,30,version=2)  # first get if not then sets   by default version 1 
#   # or
#      data={'name':'Anamika','roll':101,'course':'B.tech'}
#      cache.set_many(data,30)
#      mv=cache.get_many(data)
#      return render(request,'course.html',{'fm':mv})

#delete cache
# def home(request):
#     #cache.delete('fees') # by default will delete version 1 if want to dlete other version then need to give version
#     cache.set('roll',101,500)
#     rv=cache.decr('roll',delta=2) #delta =1 decrement by 1
#     print(rv)
#     iv=cache.incr('roll',delta=5) #will incremnt on current value
#     print(iv)
#     return render(request,'course.html')

#clear all cache
def home(request):
    cache.clear() # delete all cache
    return render(request,'course.html')
