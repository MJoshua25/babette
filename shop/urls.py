from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name="shop"),
    path('produit/<slug:titre_slug>', views.product, name="product"),
    path('Shop-cart/', views.cart, name="cart"),
]
