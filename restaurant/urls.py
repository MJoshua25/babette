from django.urls import path, re_path, include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='home'),
]


