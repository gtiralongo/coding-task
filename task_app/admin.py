from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(ModelAdmin):
    ...

# ->  NEXT vamos alos settings del project settings.py