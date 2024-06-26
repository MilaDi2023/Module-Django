from django.shortcuts import render
from .models import News_post
from .models import News_post_HomeTask

# Create your views here.

def home(request):
    news = News_post.objects.all()
    return render(request, 'lessonDJ03/news.html', {'news': news})

def home_HomeTask(request):
    news = News_post_HomeTask.objects.all()
    return render(request, 'lessonDJ03/news.html', {'news': news})