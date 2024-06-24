from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'caption': "Django Lessons"
    }
    return render(request, 'lessonDJ02/index.html', data)

def new(request):
    return render(request, 'lessonDJ02/new.html')
