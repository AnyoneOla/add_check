#-*- coding:utf-8 -*-

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# namespace
app_name = 'it_works'

urlpatterns = [
    # Create a task
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()