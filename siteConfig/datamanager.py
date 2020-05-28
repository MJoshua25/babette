from django.http.request import HttpRequest
from . import models


def getConfig(request: HttpRequest) -> dict:
    data = {
        'logo': models.Logo.objects.filter(status=True)[:1].get()
    }
    return data


def mergeData(request: HttpRequest, actual: dict) -> dict:
    actual.update(getConfig(request))
    return actual
