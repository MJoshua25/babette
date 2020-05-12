from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/index.html', data)


def event(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/events.html', data)


def eventSingle(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/event-single.html', data)


def faqs(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/faqs.html', data)


def reservation(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/reservation.html', data)


def gallery(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/gallery-grid.html', data)


def menuBoard(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/menu-board.html', data)
