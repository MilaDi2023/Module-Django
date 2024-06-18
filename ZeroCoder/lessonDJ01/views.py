from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Это главная страница домашнего задания по уроку DJ01</h1>")

def data(request):
    return HttpResponse("<h1>DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA DATA </h1>")

def test(request):
    return HttpResponse("<h1>TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST </h1>")
