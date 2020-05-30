from django.urls import path, re_path, include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.faqs, name='faqs'),
    path('menu', views.menuBoard, name='menuBoard'),
    path('reservation', views.reservation, name='reservation'),
    path('gallery', views.gallery, name='gallery'),
    path('event', views.event, name='event'),
    path('<slug:titre_slug>', views.eventSingle, name='eventSingle'),
]


