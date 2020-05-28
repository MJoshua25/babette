from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from restaurant import models as rest_models
from . import models


# TODO: Dynamisation formulaire Réservation
# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        
        place = request.POST.get('place')
        date = request.POST.get('date')
        heure = request.POST.get('heure')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        requete = request.POST.get('requete')

        c = models.Reservation(
            
            place = place,
            date = date,
            heure = heure,
            name = name,
            email = email,
            phone = phone,
            requete = requete
            )
        c.save()
        return redirect('restaurant:index')
    else:
         
        data = {
            
            'categories': rest_models.Categorie.objects.filter(status=True),
            'photo':models.Menu.objects.filter(status=True).order_by('-date_add')[:8]

       
          
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

        "faqs": rest_models.Faq.objects.filter(status=True),

    }
    return render(request, 'pages/faqs.html', data)


def reservation(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/reservation.html', data)


def gallery(request: HttpRequest) -> HttpResponse:
    data = {
        'menus': models.Menu.objects.filter(status=True),
        "categories": rest_models.Categorie.objects.filter(status=True),
    }
    print(data)
    return render(request, 'pages/gallery-grid.html', data)


def menuBoard(request: HttpRequest) -> HttpResponse:
    data = {
        'menu': models.Menu.objects.filter(status=True).order_by('-date_add')[:8],
    }
    return render(request, 'pages/menu-board.html', data)
