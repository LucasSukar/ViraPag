from django.shortcuts import render
from django.http import HttpResponse

def mainapp(request):
    return render(request, 'mainapp/mainapp.html')
