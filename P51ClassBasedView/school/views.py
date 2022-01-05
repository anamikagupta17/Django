from django.shortcuts import render
from django.http import HttpResponse
from django.views import View  #can import from generic

# Create your views here.

#function based view
def myview(req):
    return HttpResponse("<h1>Function Based View </h1>")


#view based class based view
class MyView(View):
    name='Anamika Gupta'
    def get(self,req):
        #return HttpResponse("<h1>Class Based View : GET </h1>")
        return HttpResponse(self.name)
    
    
class MyViewChild(MyView):
    def get(self,req):
        return HttpResponse(f"Child Class of Class Based View : {self.name}")
            