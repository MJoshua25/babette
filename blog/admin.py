from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
  

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

   

class TagAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
  

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]




class CommentaireAdmin(admin.ModelAdmin):
    list_display = (
        'article',
        'prenom',
        'nom',
        'email',
        'message',

        'cover',
        'status',
        'date_add',
        'date_update' 
    )

    list_filter = (
        'article',
        'status',
        'date_add',
        'date_update'
    )
    search_fields = (
        'message',
        'date_add'
    )
    fieldsets = [
        ('Info ', {'fields': [
            'article',
            'prenom',
            'nom',
            'email',
            'message',
        ]
        }),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'affiche_image',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'categorie',
        'status',
        'tags'
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': [
            'titre',
            'categorie',
            'tags',
            'contenu'
        ]
        }),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
