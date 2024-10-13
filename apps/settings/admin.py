from django.contrib import admin
from apps.settings.models import BaseSettings,Blog
# Register your models here.

admin.site.register(BaseSettings)
admin.site.register(Blog)