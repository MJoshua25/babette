from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='index'),
    path('single_blog/', views.single_blog, name='single_blog'),
]
