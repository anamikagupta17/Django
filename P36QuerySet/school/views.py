from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(req):
    students=Student.objects.all() #all data
    
    #students=Student.objects.filter(marks=80,city='Lucknow') #filter who has marks=80
    
    #students=Student.objects.exclude(marks=90)  #return marks not in 90
    
    #students=Student.objects.order_by('-city') # - descending order, 
    
    #students=Student.objects.order_by('?') # random records
    #students=Student.objects.order_by('id').reverse()[:2] # reverse the sequence [:2] limit 
    
    
    #students=Student.objects.values()
    #students=Student.objects.values('name','city')
    
    #students=Student.objects.values_list(named=True) # return in tuples named shoud be true if need column name in case tuples
    #students=Student.objects.using('default') #default db 
    
    #students=Student.objects.dates('pass_date','month')
    
    #-------------Second Table --------------------
    
    qs1=Student.objects.values_list('id','name',named=True)
    qs2=Teacher.objects.values_list('id','name',named=True)
    
    #students=qs2.union(qs1,all=True) #combine all True will get all data if false then no duplicate
    #students=qs2.intersection(qs1) # only matched data
    
    #students=qs2.difference(qs1) # not mactched data  
    
    
    #----------Operators-----------
    #students=Student.objects.filter(marks=80) & Student.objects.filter(city='Lucknow')
    
    #students=Student.objects.filter(Q(marks=80)& Q(city='Lucknow'))
    
    #students=Student.objects.filter(marks=80) | Student.objects.filter(city='Lucknow')
    #students=Student.objects.filter(Q(marks=80)|Q(city='Lucknow'))
    
    
    # these all return query set 
    
    print('Query Set Data : ',students)
    print('Sql Query : ',students.query) # get the query
    return render(req,'home.html',{'students':students})