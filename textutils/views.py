from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('new line remover','off')
    spaceremover=request.POST.get('space remover','off')
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        a=""
        for char in djtext:
            if char not in punctuations:
                a=a+char
        params={'purpose':'Removed Punctuations','ch':a}
        djtext=a
    if fullcaps=='on':
        a=""
        for char in djtext:
            a=a+char.upper()
        params = {'purpose': 'All characters to Uppercase', 'ch': a}
        djtext=a
    if newlineremover=='on':
        a=""
        for char in djtext:
            if char not in '\n' and char!='\r':
                a=a+char
        params = {'purpose': 'New line remover', 'ch': a}
        djtext=a
    if spaceremover=='on':
        a=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                a=a+char
        params = {'purpose': 'space remover', 'ch': a}
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and spaceremover!='on'):
        return HttpResponse("select any operation on yuor text to be performed")
    return render(request,'analyze.html',params)

