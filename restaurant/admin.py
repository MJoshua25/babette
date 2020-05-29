from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# TODO: Admin models Réservation et physique data
# Register your models here.

class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'reponse',
        'status',
        'date_add',
        'date_update',

    )
    list_filter = (
        'status',
        'date_add',
        'date_update'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['question', 'reponse',
                              ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


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
        'date_update'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['titre',
                              ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update'

    )
    list_filter = (
        'status',
        'date_add',
        'date_update'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['titre',
                              ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'categorie',
        'isrecommended',
        'prix',
        'affiche_image',
        'status',
        'date_add',
        'date_update'

    )
    list_filter = (
        'status',
        'date_add'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', 'categorie',
                              'ingredients',
                              'isrecommended',
                              'prix', ]}),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'place',
        'date',
        'heure',
        'name',
        'email',
        'phone',
        'status',
        'date_add',
        'date_update'

    )
    list_filter = (
        'name',

        'status',
        'date_add',
        'date_update'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['place',
                              'date',
                              'heure',
                              'name',
                              'email',
                              'phone', 'requete', ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

class TitreguestAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'soustitre',
        'status',
        'date_add',
        'date_update'

    )
    list_filter = (
        'status',
        'date_add',
        'date_update'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['titre','soustitre',
                              ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class GuestAdmin(admin.ModelAdmin):
    list_display = (
       
        'nom',
        'metier',
        'message',
        'affiche_image',
        'status',
        'date_add',
        'date_update'

    )
    list_filter = (
        'status',
        'date_add'

    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': [
        'nom',
        'metier',
        'message',]}),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Faq, FaqAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Ingredient, IngredientAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Reservation, ReservationAdmin)
_register(models.Guest, GuestAdmin)
_register(models.Titreguest, TitreguestAdmin)