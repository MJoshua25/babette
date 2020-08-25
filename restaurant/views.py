from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from restaurant import models as rest_models
from siteConfig.datamanager import mergeData
import datetime
from . import models


def isOpen(date: datetime.datetime) -> bool:
    aux = date.isoweekday()
    if aux == 1 or aux < 6:
        dayVerif = models.Phydata.objects.filter(jours='1').get()
    else:
        dayVerif = models.Phydata.objects.filter(jours=str(aux)).get()
    return dayVerif.isOpen


def getHeureDebut(date: datetime.datetime) -> bool:
    aux = date.isoweekday()
    if aux == 1 or aux < 6:
        dayVerif = models.Phydata.objects.filter(jours='1').get()
    else:
        dayVerif = models.Phydata.objects.filter(jours=str(aux)).get()
    return dayVerif.getDateTimeHeureDebut


def getHeureFin(date: datetime.datetime) -> bool:
    aux = date.isoweekday()
    if aux == 1 or aux < 6:
        dayVerif = models.Phydata.objects.filter(jours='1').get()
    else:
        dayVerif = models.Phydata.objects.filter(jours=str(aux)).get()
    return dayVerif.getDateTimeHeureFin


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

            place=place,
            date=date,
            heure=heure,
            name=name,
            email=email,
            phone=phone,
            requete=requete
        )
        c.save()
        return redirect('restaurant:index')
    else:
        demain = datetime.datetime.now() + datetime.timedelta(days=1)
        heureFin = 0
        heureDebut = 0
        i = 1
        li = []
        while len(li) < 5:
            print(i, demain)
            if isOpen(demain):
                print('enter')
                if len(li) == 0:
                    heureDebut = getHeureDebut(demain)
                    heureFin = getHeureFin(demain)
                else:
                    heureDebut = heureDebut if getHeureDebut(demain) < heureDebut else getHeureDebut(demain)
                    heureFin = heureFin if getHeureFin(demain) > heureFin else getHeureFin(demain)
                li.append({
                    'libelle': demain,
                    'value': i,
                })
            i += 1
            demain = demain + datetime.timedelta(days=1)
        heureFin = heureFin if datetime.datetime.combine(datetime.date.today(), datetime.time(23, 0,
                                                                                              0)) > heureFin else datetime.datetime.combine(
            datetime.date.today(), datetime.time(23, 0, 0))
        hours = []
        while heureDebut < heureFin:
            hours.append({
                'libelle': heureDebut,
                'value': heureDebut.hour,
            })
            heureDebut += datetime.timedelta(hours=1)
        formData = {
            'people': range(1, 8),
            'days': li,
            'hours': hours
        }
        data = {
            'categories': rest_models.Categorie.objects.filter(status=True),
            'guests': models.Guest.objects.filter(status=True),
            'titreguests': models.Titreguest.objects.filter(status=True),
            'phydatas': models.Phydata.objects.filter(status=True).order_by('-date_add'),
            'tels': models.Tel.objects.filter(status=True),
            'formData': formData,
            'photo': models.Menu.objects.filter(status=True).order_by('-date_add')[:8],
            'event': models.Event.objects.filter(status=True)
        }
        return render(request, 'pages/index.html', mergeData(request, data))


def eventSingle(request: HttpRequest, titre_slug: str) -> HttpResponse:
    data = {
        'evsing': rest_models.Event.objects.filter(status=True, titre_slug=titre_slug)[:1].get()

    }
    return render(request, 'pages/event-single.html', data)


def event(request: HttpRequest) -> HttpResponse:
    data = {
        'events': models.Menu.objects.filter(status=True).order_by('-date_add')[:8],
    }
    return render(request, 'pages/events.html', data)


def faqs(request: HttpRequest) -> HttpResponse:
    data = {

        "faqs": rest_models.Faq.objects.filter(status=True),

    }
    return render(request, 'pages/faqs.html', mergeData(request, data))


def reservation(request: HttpRequest) -> HttpResponse:
    data = {
    }
    return render(request, 'pages/reservation.html', mergeData(request, data))


def gallery(request: HttpRequest) -> HttpResponse:
    data = {
        'menus': models.Menu.objects.filter(status=True),
        "categories": rest_models.Categorie.objects.filter(status=True),
    }
    return render(request, 'pages/gallery-grid.html', mergeData(request, data))


def menuBoard(request: HttpRequest) -> HttpResponse:
    data = {
        'menu': models.Menu.objects.filter(status=True).order_by('-date_add')[:8],
    }
    return render(request, 'pages/menu-board.html', mergeData(request, data))
