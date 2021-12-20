from django.shortcuts import render


class UnderConstructionSite:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        print('Call from Middleware: before view')  
        #response=self.get_response(request) #this will call view
        response=render(request,'under.html') #will not call view show underconstruction
        print('Call from Middleware : after view')  
        return response  
    
  