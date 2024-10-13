from django.shortcuts import render
from apps.settings.models import BaseSettings,Blog
# Create your views here.

def settings(request):
    setting = BaseSettings.objects.latest('id')
    blogs = Blog.objects.all()
    return render(request, 'index.html', locals())
