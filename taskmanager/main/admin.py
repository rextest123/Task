from django.contrib import admin

# Register your models here.

from .models import Task, Items, Docs, Tasks

admin.site.register(Task)
admin.site.register(Items)
admin.site.register(Docs)
admin.site.register(Tasks)