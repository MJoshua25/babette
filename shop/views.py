from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from restaurant import models as rest_models
from django.core.paginator import Paginator
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def shop(request: HttpRequest) -> HttpResponse:
    produits = models.Produit.objects.filter(status=True)
    paginator = Paginator(produits, 3)
    page = request.GET.get('page')
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    data = {
        "categories": models.Categorie.objects.filter(status=True),
        'produits': p,
    }
    print(data)
    return render(request, 'pages/shop/shop.html', data)


def cart(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shopping-cart.html', data)


def product(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shop-single-product.html', data)
