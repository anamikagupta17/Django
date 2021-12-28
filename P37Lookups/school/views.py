from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from .models import Student
from datetime import date,time

# Create your views here.

def home(req):
    students=Student.objects.all()
    #---------------lookeups-------------
    
    #students=Student.objects.filter(name__exact='Mansi') #case sensitive
    #students=Student.objects.filter(name__iexact='parul') #case insensitive
    #students=Student.objects.filter(name__contains='a')  #some time work case sensitive sometime not
    #students=Student.objects.filter(name__icontains='u')  
    #students=Student.objects.filter(id__in=[1,4,2,5]) 
    #students=Student.objects.filter(marks__in=[96])   
    
    # students=Student.objects.filter(marks__gt=80) #grater than
    # students=Student.objects.filter(marks__gte=89) #grater than and  equeal
    # students=Student.objects.filter(marks__lt=89)#less than
    # students=Student.objects.filter(marks__lte=80)#less than and  equeal
    
    # students=Student.objects.filter(name__startswith='m')
    # students=Student.objects.filter(name__istartswith='m')
    # students=Student.objects.filter(name__endswith='i')
    # students=Student.objects.filter(name__iendswith='I')
    #students=Student.objects.filter(pass_date__range=('2021-10-10','2021-12-27'))
    #students=Student.objects.filter(admit_date__date=date(2020, 1, 1)) # date will work  datetime
    
    #students=Student.objects.filter(admit_date__date__gt=date(2021, 1, 1)) # date will work  datetime
    
    # students=Student.objects.filter(pass_date__year=2020)
    # students=Student.objects.filter(pass_date__year__gt=2020)
    # students=Student.objects.filter(pass_date__year__gte=2020)
    
    # students=Student.objects.filter(pass_date__month=11)
    # students=Student.objects.filter(pass_date__month__gt=10)
    # students=Student.objects.filter(pass_date__month__gte=10)
    
    # students=Student.objects.filter(pass_date__day=1)
    # students=Student.objects.filter(pass_date__day__gt=1)
    # students=Student.objects.filter(pass_date__day__gte=5)
    
    # students=Student.objects.filter(pass_date__week=1)
    # students=Student.objects.filter(pass_date__week__gt=5)
    # students=Student.objects.filter(pass_date__week__gte=1)
    
    # students=Student.objects.filter(pass_date__week_day=1)  #1 sunday
    # students=Student.objects.filter(pass_date__week_day=3)   #tuseday
    # students=Student.objects.filter(pass_date__week_day__gte=4) 
    
    #students=Student.objects.filter(pass_date__quarter=3) 
    # students=Student.objects.filter(admit_date__time__gt=time(19,00)) 
    # students=Student.objects.filter(admit_date__hour=10) 
    # students=Student.objects.filter(admit_date__minute=41) 
    # students=Student.objects.filter(admit_date__second__gte=12)
    # students=Student.objects.filter(roll__isnull=True)
    # students=Student.objects.filter(roll__isnull=False)
    
    print("Return Data :",students)
    print('--------------------')
    print("Query : ",students.query)
    return render(req,'home.html',{'students':students})
