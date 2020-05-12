from django.contrib import admin
from django.urls import path, include
from  . import views


urlpatterns = [
    path('shop/',views.shop,name="shop"),
    path('shop-product/',views.product,name="product"),
    path('Shop-cart/',views.cart,name="cart"),
]
