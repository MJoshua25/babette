from django.http.request import HttpRequest
from . import models


def getConfig(request: HttpRequest) -> dict:
    data = {
        'logo': models.Logo.objects.filter(status=True)[:1].get(),
        "ouvertures": models.Ouverture.objects.filter(status=True),
        "footers": models.Footer.objects.filter(status=True),
        "sponsors": models.Sponsor.objects.filter(status=True),
        "mainevents": models.Mainevent.objects.filter(status=True),
        
    }
    return data


def mergeData(request: HttpRequest, actual: dict) -> dict:
    actual.update(getConfig(request))
    return actual
