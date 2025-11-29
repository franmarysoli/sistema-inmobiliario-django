from django.contrib import admin
from .models import TipoPropiedad, Ubicacion, Propiedad

# Register your models here.

@admin.register(TipoPropiedad)
class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'estado', 'zona')
    search_fields = ('ciudad', 'estado', 'zona')
    list_filter = ('estado', 'ciudad')


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'precio', 'estado', 'habitaciones', 'baños', 'destacada', 'fecha_publicacion')
    list_filter = ('estado', 'tipo', 'destacada', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion', 'ubicacion__ciudad')
    list_editable = ('destacada', 'estado')
    readonly_fields = ('fecha_publicacion', 'fecha_actualizacion')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion', 'tipo', 'ubicacion')
        }),
        ('Características', {
            'fields': ('precio', 'area_metros', 'habitaciones', 'baños', 'estacionamientos')
        }),
        ('Estado y Publicación', {
            'fields': ('estado', 'destacada', 'imagen', 'fecha_publicacion', 'fecha_actualizacion')
        }),
    )
