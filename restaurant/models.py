from django.db import models
import datetime
from django.db.models.query import QuerySet
import pytz
from tinymce import HTMLField
from django.utils.translation import ugettext as _

DAY_OF_THE_WEEK = {
    '1': _(u'Monday'),
    '2': _(u'Tuesday'),
    '3': _(u'Wednesday'),
    '4': _(u'Thursday'),
    '5': _(u'Friday'),
    '6': _(u'Saturday'),
    '7': _(u'Sunday'),
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=255)
    reponse = models.CharField(max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Faq"
        verbose_name_plural = "Faqs"

    def __str__(self):
        return str(self.question)


class Categorie(models.Model):
    titre = models.CharField(max_length=255, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return str(self.titre)

    @property
    def getMenus(self) -> QuerySet:
        return self.menus.filter(status=True)

    @property
    def getMenusTwoPart(self) -> list:
        if len(self.getMenus) > 0:
            return [self.getMenus[:(self.getMenus.count() // 2)],
                    self.getMenus[(self.getMenus.count() // 2):]]
        else:
            return []


class Ingredient(models.Model):
    titre = models.CharField(max_length=255, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self) -> str:
        return str(self.titre)


class Menu(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='menus')
    titre = models.CharField(max_length=255, unique=True)
    cover = models.ImageField('restaurant/menu')
    ingredients = models.ManyToManyField(Ingredient, related_name='menus')
    isrecommended = models.BooleanField(default=False)
    prix = models.FloatField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return str(self.titre)

    @property
    def isNew(self) -> bool:
        now = datetime.datetime.now()
        now = pytz.utc.localize(now)
        return (now - self.date_add).days < 30

    @property
    def getIngredients(self) -> QuerySet:
        return self.ingredients.filter(status=True)


# TODO: Model Réservation et Physique_data

class Reservation(models.Model):
    place = models.IntegerField(default=1)
    date = models.DateTimeField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    requete = models.TextField(blank=True, null=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Reservation")
        verbose_name_plural = ("Reservations")

    def __str__(self):
        return self.name


class Titreguest(models.Model):
    titre = models.CharField(max_length=255, unique=True)
    soustitre = models.CharField(max_length=255, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Titreguest"
        verbose_name_plural = "Titreguests"

    def __str__(self):
        return str(self.titre)

    @property
    def getGuests(self) -> QuerySet:
        return self.guests.filter(status=True)


class Guest(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    metier = models.CharField(max_length=255, unique=True)
    message = models.TextField()
    cover = models.ImageField('restaurant/ourgest')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"

    def __str__(self):
        return str(self.nom)


class Tel(models.Model):
    titre = models.CharField(max_length=255, unique=True)
    dispo = models.CharField(max_length=255, unique=True)
    call = models.CharField(max_length=255, unique=True)
    tel = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tel"
        verbose_name_plural = "Tels"

    def __str__(self):
        return str(self.titre)


class Phydata(models.Model):
    jours = DayOfTheWeekField()
    hdebut = models.TimeField(null=True, blank=True)
    hfin = models.TimeField(null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Phydata"
        verbose_name_plural = "Phydatas"

    @property
    def afficheHeure(self) -> tuple:
        nom = "Weekdays" if self.jours == '1' else self.jours
        heure = "{} - {}".format(self.hdebut, self.hfin) if self.hdebut is not None else "Fermé"
        return nom, heure

    def __str__(self):
        return str(self.jours)


class Ticket(models.Model):
    titre = models.CharField(max_length=50, unique=True)
    ticket = models.IntegerField()
    tick_rest = models.IntegerField()
    prix = models.FloatField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.titre


class Event(models.Model):
    titre = models.CharField(max_length=50)
    cover = models.ImageField('events/images')
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    date_deb = models.DateField()
    date_fin = models.DateField()
    ticket = models.ManyToManyField(Ticket, related_name='Events')
    description = HTMLField('events/description')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.titre
