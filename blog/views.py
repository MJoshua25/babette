from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models


# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
    data = {
        'article': models.Article.objects.filter(status=True).order_by('-date_add')[:6]
    }
    return render(request, 'pages/blog/blog-carousel.html', data)


def single_blog(request: HttpRequest, titre_slug: str) -> HttpResponse:
    data = {
        'categories': models.Categorie.objects.filter(status=True).order_by('-date_add')[:6],
        'articles': models.Article.objects.filter(status=True).order_by('-date_add')[:2],
        'single': models.Article.objects.filter(titre_slug=titre_slug)[:1].get(),
    }
    return render(request, 'pages/blog/blog-single-post.html', data)
