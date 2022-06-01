from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('call', views.call, name='call'),
    path('tasks', views.tasks, name='tasks'),
    path('items', views.items, name='item'),
    path('admin', admin.site.urls, name='admin')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)