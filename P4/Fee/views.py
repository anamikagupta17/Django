from django.shortcuts import render

def feeDjango(request):
     return render(request,'fees/feeOne.html')
def feePython(request):
     return render(request,'fees/feeTwo.html',{'fee':20000})