from django.shortcuts import render

def index(request):
    return render(request, 'HomeTaskDJ02/index.html')

def about(request):
    return render(request, 'HomeTaskDJ02/about.html')

def services(request):
    return render(request, 'HomeTaskDJ02/services.html')

def contact(request):
    return render(request, 'HomeTaskDJ02/contact.html')
