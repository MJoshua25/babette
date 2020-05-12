from django.shortcuts import render

# Create your views here.

def shop(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shop.html', data)


def cart(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shop-cart.html', data)



def product(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/shop/shop-single-product.html', data)