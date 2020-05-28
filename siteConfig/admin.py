from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

class AffichmenuAdmin(admin.ModelAdmin):
    list_display = (
        'head',
        'titre',
        'message',
        'affiche_image',
        'status',
        'date_add',
        
        
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
        ('Info ', {'fields': ['head',
        'titre',
        'message',]}),
        ('Image', {'fields': ['cover', 'affiche_image',]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]
    
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))
   
    
class MaineventAdmin(admin.ModelAdmin):
    list_display = (
        'head',
        'titre',
        'message',
        'affiche_image',
        'status',
        'date_add',
        
        
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
        ('Info ', {'fields': ['head',
        'titre',
        'message',]}),
        ('Image', {'fields': ['cover', 'affiche_image',]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]
    
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))
                                 


class OuvertureAdmin(admin.ModelAdmin):
    list_display = (
        'head',
        'titre',
        'message',
        'affiche_image',
        'status',
        'date_add',
        
        
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
        ('Info ', {'fields': ['head',
        'titre',
        'message',]}),
        ('Image', {'fields': ['cover', 'affiche_image',]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]
    
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))
    

class FooterAdmin(admin.ModelAdmin):
        
    list_display = (
        
        'adress',
        'jours',
        'message',
        'email',
        'tel',
        
        
        'status',
        'date',
    )

    list_filter = (
        'status',
    )
    search_fields = (
        'status',
    )
    list_per_pages = 50
    date_hierarchy = 'date'
    
    fieldsets = [
        ('Info ', {'fields': [
        'adress',
        'jours',
        'message',
        'email',
        'tel',
        'date',
        ]
        }),
        
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class LogoAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'affiche_image_dark',
        'affiche_image_light',
        'status',
        'date_add',
        'date_upd'
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
    readonly_fields = ['affiche_image_dark', 'affiche_image_light']

    fieldsets = [
        ('Info ', {'fields': ['titre',]}),
        ('Image', {'fields': ['logo_dark','affiche_image_dark', 'logo_light','affiche_image_light', ]}),
        ('Status et Activations', {'fields': ['status', ]}),]

    def affiche_image_dark(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.logo_dark.url))

    def affiche_image_light(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.logo_light.url))
    
    
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Ouverture, OuvertureAdmin)
_register(models.Affichmenu, AffichmenuAdmin)
_register(models.Mainevent, MaineventAdmin)
_register(models.Footer, FooterAdmin)
_register(models.Logo, LogoAdmin)