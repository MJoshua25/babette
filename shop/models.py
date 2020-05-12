from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Produit_Tag(models.Model):
    
    titre = models.CharField(max_length=50, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit_Tag"
        verbose_name_plural = "Produit_Tags"

    def __str__(self) -> str:
        return str(self.titre)



class Produit(models.Model):

    tag=models.ManyToManyField(Produit_Tag,related_name='prodtag')
    titre = models.CharField(max_length=50)
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    cover = models.ImageField(upload_to='Shop/Produits')
    prix=models.FloatField()

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


class Commande(models.Model):

    client = models.OneToOneField(User,on_delete=models.CASCADE)
    produit=models.ManyToManyField(Produit,related_name='commande')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self) -> str:
        return str(self.titre)