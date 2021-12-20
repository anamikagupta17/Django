from django.shortcuts import HttpResponse



class MyMiddleware:
    def __init__(self,get_response):  #one time
        self.get_response=get_response
        print('One Time Initialization class based')
    
    def __call__(self,request):  # every request
        print("this is before view class")
        response=self.get_response(request)   
        print("this is after view class")
        return response 
    
    
class BrotherMiddleware:
    def __init__(self,get_response):  #one time
        self.get_response=get_response 
        print('One Time Initialization Brother')
    
    def __call__(self,request):  # every request
        print("this is before view class Brother")
        response=self.get_response(request)    #goes to next middleware 
        print("this is after view class Brother")
        return response     
    
    
    
class FatherMiddleware:
    def __init__(self,get_response):  #one time
        self.get_response=get_response 
        print('One Time Initialization Father')
    
    def __call__(self,request):  # every request
        print("this is before view class Father")
        response=self.get_response(request)     #goes to next middleware 
        #response=HttpResponse('Nikal lo')  #if you want give response here don't want to send next 
        print("this is after view class Father")
        return response     
    
    
    
    
class MotherMiddleware:
    def __init__(self,get_response):  #one time
        self.get_response=get_response 
        print('One Time Initialization Mother')
    
    def __call__(self,request):  # every request
        print("this is before view class Mother")
        response=self.get_response(request)  #goes to view because no next middileware  
        print("this is after view class Mother")
        return response             
    
    
    
#hooks

class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
            
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        print('This is process view before view')
        #return HttpResponse("this is before view -hooks")  #it will return from here will not callview
        return None #this will go to view       
    
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
            
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        print('This is Exception view before view')
        msg=exception
        print('Class Name :',exception.__class__.__name__)
        return HttpResponse(msg)  #it will return from here will not callview
    
    
class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
            
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        print('This is Template Response view before view')
        response.context_data['name']="Parul Gupta" # change name given in view
        return response
    
                    
                