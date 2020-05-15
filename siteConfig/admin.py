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
    
    
    
def _register(model, admin_class):
        admin.site.register(model, admin_class)


_register(models.Ouverture, OuvertureAdmin)
_register(models.Affichmenu, AffichmenuAdmin)
_register(models.Mainevent, MaineventAdmin)
