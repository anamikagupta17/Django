from django.shortcuts import render

# Create your views here.
def home(request):
    ct=request.session.get('count',0)
    newCt=ct+1
    request.session['count']=newCt
    return render(request,'home.html',{'c':newCt})
    