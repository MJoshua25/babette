from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from siteConfig import models as rest_models
from . import models


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    data = {
    
       
        "affichmenus": models.Affichmenu.objects.filter(status=True),
        "mainevents": models.Mainevent.objects.filter(status=True),
       

    }
    return render(request, 'pages/index.html', data)