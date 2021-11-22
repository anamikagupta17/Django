from django.shortcuts import render

def languageOne(request):
     return render(request,'languageOne.html',{'lang':'PHP'})
def languageTwo(request):
     return render(request,'languageTwo.html')