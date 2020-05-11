from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/index.html', data)
