from django.shortcuts import render


def learnDjango(request):
    return render(request,'courseOne.html')
def learnPython(request):
    courses={'cname':'Python','duration':'5 months'}
    return render(request,'courseTwo.html',courses)