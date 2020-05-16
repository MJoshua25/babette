from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


class Ouverture(models.Model):
    
    head = models.CharField(max_length=50, unique=True)    
    titre = models.CharField(max_length=50, unique=True)
    message = models.TextField()
    cover = models.ImageField(upload_to='ouvertures')
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        verbose_name = "Ouverture"
        verbose_name_plural = "Ouvertures"

    def __str__(self) -> str:
        return str(self.titre)
    

class Affichmenu(models.Model):
    
    head = models.CharField(max_length=50, unique=True)    
    titre = models.CharField(max_length=50, unique=True)
    message = models.TextField()
    cover = models.ImageField(upload_to='ouvertures')
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        verbose_name = "Affiche menu"
        verbose_name_plural = "Affiche menus"

    def __str__(self) -> str:
        return str(self.titre)
    
    
    
class Mainevent(models.Model):
    
    head = models.CharField(max_length=50, unique=True)    
    titre = models.CharField(max_length=50, unique=True)
    message = models.TextField()
    cover = models.ImageField(upload_to='mainevent')
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        verbose_name = "Main event"
        verbose_name_plural = "Main events"

    def __str__(self) -> str:
        return str(self.titre)    
    
 
class Footer(models.Model):
    
    adress = models.CharField(max_length=50, unique=True)
    jours = models.CharField(max_length=50, unique=True)    
    email = models.EmailField()
    message = models.TextField()
    tel = models.CharField(max_length=50, unique=True)  
    status = models.BooleanField(default=True)
    date = models.DateTimeField()
   

    class Meta:
        verbose_name = "footer"
        verbose_name_plural = "footers"

    def __str__(self) -> str:
        return str(self.date)       
    