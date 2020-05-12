from django.db import models


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
    titre = models.CharField(max_length=255, unique=True)
    cover = models.ImageField('restaurant/menu')
    ingredients = models.ManyToManyField(related_name='menus')
    isrecommended = models.BooleanField()
    prix = models.FloatField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return str(self.titre)
