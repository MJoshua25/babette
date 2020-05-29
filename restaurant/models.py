from django.db import models
import datetime
from django.db.models.query import QuerySet
import pytz


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
    
    place = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    heure = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    requete = models.TextField(blank=True,null=True)

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