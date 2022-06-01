from django.contrib import admin

# Register your models here.

from .models import Task, Items

admin.site.register(Task)
admin.site.register(Items)