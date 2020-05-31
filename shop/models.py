from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


# Create your models here.


class Tag(models.Model):
    titre = models.CharField(max_length=255, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return str(self.titre)


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
    def getProduits(self) -> QuerySet:
        return self.produits.filter(status=True)


class Produit(models.Model):
    tag = models.ManyToManyField(Tag, related_name='produits')
    categories = models.ManyToManyField(Categorie, related_name='produits')
    titre = models.CharField(max_length=50)
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    cover = models.ImageField(upload_to='Shop/Produits')
    prix = models.FloatField()
    contenu = HTMLField('Content')
    description = HTMLField('Content/description')
    information = HTMLField('Content/information')
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self) -> str:
        return str(self.titre)

    def save(self, *args, **kwargs):
        super(Produit, self).save(*args, **kwargs)
        encoding_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(str(self.titre) + ' ' + str(encoding_id.hexdigest()))
        super(Produit, self).save(*args, **kwargs)

    @property
    def getTags(self) -> QuerySet:
        return self.tag.filter(status=True)

    @property
    def getCategories(self) -> QuerySet:
        return self.categories.filter(status=True)


class Review(models.Model):
    """Model definition for Review."""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    review = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of Review."""
        return self.name


class Commande(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name='commandes')
    produit = models.ManyToManyField(Produit, related_name='commandes', through='CommandeContenu')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self) -> str:
        return str(self.client)




class CommandeContenu(models.Model):
    commande = models.ForeignKey(Commande, related_name='contenu', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='commandes_contenu', on_delete=models.CASCADE)
    prixUnitaire = models.IntegerField(default=0)
    quantité = models.IntegerField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CommandeContenu"
        verbose_name_plural = "CommandeContenus"

    def __str__(self):
        return '{}: ({}){}'.format(self.commande, self.quantité, self.produit)
