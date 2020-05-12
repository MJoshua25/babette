from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models


# Create your views here.





def blog(request: HttpRequest) -> HttpResponse:
    data = {
        

    }
    return render(request, 'pages/blog-carousel.html', data)

def single_blog(request: HttpRequest) -> HttpResponse:
    data = {
        

    }
    return render(request, 'pages/blog-single-post.html', data)