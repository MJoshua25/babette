from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models


# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
    data = {
        'article': models.Article.objects.filter(status=True).order_by('- date_add')[:6]
    }
    return render(request, 'pages/blog/blog-carousel.html', data)


def single_blog(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/blog/blog-single-post.html', data)
