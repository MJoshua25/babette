from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from restaurant import models as rest_models
from django.core.paginator import Paginator
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def shop(request: HttpRequest) -> HttpResponse:
    produits = models.Produit.objects.filter(status=True),
    p = Paginator(produits, 3)
    print(p, p.count, p.num_pages, p.page_range)
    page_number = request.GET.get('page')
    if not page_number:
        print('test')
        page_obj = p.get_page(1)
    print(page_number)

    print(page_obj, type(page_obj))
    for i in page_obj.object_list:
        print('1')
    print(page_obj.object_list)
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
