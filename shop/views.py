from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from restaurant import models as rest_models
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def shop(request: HttpRequest) -> HttpResponse:
    data = {
        "categories": models.Categorie.objects.filter(status=True),
        'produits': models.Produit.objects.filter(status=True),

    }
    print(data)
    return render(request, 'pages/shop/shop.html', data)


def cart(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shop-cart.html', data)


def product(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shop-single-product.html', data)
