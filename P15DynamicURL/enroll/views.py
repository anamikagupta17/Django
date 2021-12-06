from django.shortcuts import render
# Create your views here.
def home(req,check):
    print(check)
    return render(req,'home.html')

def show(request,my_id):
    return render(request,'show.html',{'id':my_id})

def showOnlyId(request,my_id=1): #we can also give by default value
    if my_id==1:
       student={'id':my_id,'name':'Anamika Gupta'}
    if my_id==2:
       student={'id':my_id,'name':'Pramod Gupta'} 
    if my_id==3:
       student={'id':my_id,'name':'Parul Gupta'} 
       
            
    return render(request,'show.html',student)


def showSubId(request,my_id,sub_id):
    if my_id==1 and sub_id==1:
       student={'id':my_id,'name':'Anamika Gupta','info':'Sub Deatil'}
    if my_id==2 and sub_id==2:
       student={'id':my_id,'name':'Pramod Gupta','info':'Sub Deatil'} 
    if my_id==3 and sub_id==3:
       student={'id':my_id,'name':'Parul Gupta','info':'Sub Deatil'}      
    return render(request,'show.html',student)
