from django.contrib import admin
from .models import News_post
from .models import News_post_HomeTask

# Register your models here.

admin.site.register(News_post)
admin.site.register(News_post_HomeTask)
