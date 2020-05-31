from django.http.request import HttpRequest
from . import models
from shop import models as shop_models


def getCard(request: HttpRequest):
    try:
        card = shop_models.Commande.objects.get(id=request.session['card'])
    except:
        card = None
    return card


def getConfig(request: HttpRequest) -> dict:
    data = {
        'logo': models.Logo.objects.filter(status=True)[:1].get(),
        "ouvertures": models.Ouverture.objects.filter(status=True),
        "footers": models.Footer.objects.filter(status=True),
        "sponsors": models.Sponsor.objects.filter(status=True),
        "mainevents": models.Mainevent.objects.filter(status=True),
        "card": getCard(request)
    }
    return data


def mergeData(request: HttpRequest, actual: dict) -> dict:
    actual.update(getConfig(request))
    return actual
