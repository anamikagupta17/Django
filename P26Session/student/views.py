from django.shortcuts import render

# Create your views here.
def home(reuest):
    return render(reuest,'home.html')

def setsession(request):
    request.session['name']='Anamika Gupta'
    request.session['name2']='Parul Gupta'
    
    #few methods
    request.session.set_expiry(500)  # this will expire session in 500 sec 
    #request.session.set_expiry(0): set bowser close True
    
    return render(request,'set.html')

def getsession(request):
    #name=request.session['name']
    name=request.session.get('name','Default Gupta')
    name2=request.session.get('name2')
    
    # other methods
    keys=request.session.keys()
    items=request.session.items()
    age=request.session.setdefault('age','25') #this used for both set and get
    
    #few more methods
    
    
    return render(request,'get.html',{'name':name,'name2':name2,'keys':keys,'items':items,'age':age})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        return render(request,'del.html')
    
def flushsession(request):
    if 'name' in request.session:
        request.session.flush()
        request.session.clear_expired() # delete all expire data from db
        return render(request,'home.html')    
    
    
    
# check test cookies that bowoser supporting cookies or not means cookies enable or not    


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'settestcook.html')  

def checktestcookie(request):
    return render(request,'checktestcook.html') 

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'deltestcook.html')  

