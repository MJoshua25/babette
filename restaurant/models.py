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
