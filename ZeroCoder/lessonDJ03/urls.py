from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_HomeTask, name='lessonDJ03_home'),
]
