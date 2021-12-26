from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(req):
    students=Student.objects.get(id=2)  #pk=1,name,id..coulm shoud be unique
    #students=Student.objects.first() 
    
    #students=Student.objects.order_by('-name').first()  
    
    #students=Student.objects.order_by('-name').last()  
    
    #students=Student.objects.latest('pass_date')  
    
    #students=Student.objects.earliest('pass_date')  
    
    # students=Student.objects.all()
    # print(students.exists()) # return True if data present
    # one_data=Student.objects.get(id=2)
    
    # print(students.filter(pk=one_data.pk).exists()) # return true if exist
    
    #students=Student.objects.create(name='sumeer',roll=107,city='Bangalore',marks=84,pass_date='2021-10-12') #insert new data
    
    # students,created=Student.objects.get_or_create(name='Nisha',roll=108,city='Bangalore',marks=84,pass_date='2021-10-12')
    # print(created) # print True if ceated new
    
    #students=Student.objects.filter(name='Anamika').update(city='Lucknow')
    
    # students,created=Student.objects.update_or_create(id=8,name='Nisha',defaults={'name':'Neetu'})
    # print(created)
    
    # objs=[
    #     Student(name='Nisha',roll=109,city='Bangalore',marks=84,pass_date='2021-10-12'),
    #     Student(name='Vishal',roll=110,city='Ajamgarh',marks=74,pass_date='2021-10-12'),
    #     Student(name='Princi',roll=111,city='Mirjapur',marks=54,pass_date='2021-10-12'),
    #     Student(name='Pramod',roll=112,city='Bangalore',marks=94,pass_date='2021-10-12')
    #     ]
    # students=Student.objects.bulk_create(objs)
    
    # student_data=Student.objects.all()
    # for stu in student_data:
    #     stu.city='Bangalore'
    # students=  Student.objects.bulk_update(student_data,['city']) 
    
    # students=Student.objects.in_bulk([1,2,4]) #pk
    
    # print(students[1].name)
    # print(students[4].name)
    
    
    # students=Student.objects.in_bulk([]) # rteun empty
   
    # students=Student.objects.in_bulk() # rteun all
    # print(students)
    
    #students=Student.objects.get(pk=10).delete() # single delete
    # students=Student.objects.filter(marks=67).delete()  # delete marks=67
    
    # students=Student.objects.all().delete()  # will delete all data
    
    # students=Student.objects.all()
    # print(students.count())
    # print(students.explain())
    
    
    return render(req,'home.html',{'student':students})