from django.db import models

# Create your models here.

class TipoPropiedad(models.Model):
    """Modelo para tipos de propiedades (Casa, Apartamento, Local, etc.)"""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Tipo de Propiedad"
        verbose_name_plural = "Tipos de Propiedades"
    
    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    """Modelo para ubicaciones de las propiedades"""
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    direccion = models.TextField()
    
    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"
    
    def __str__(self):
        return f"{self.zona}, {self.ciudad}"


class Propiedad(models.Model):
    """Modelo principal para propiedades inmobiliarias"""
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('vendida', 'Vendida'),
        ('alquilada', 'Alquilada'),
        ('reservada', 'Reservada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.ForeignKey(TipoPropiedad, on_delete=models.PROTECT, related_name='propiedades')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='propiedades')
    
    # Características
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    area_metros = models.DecimalField(max_digits=8, decimal_places=2, help_text="Área en metros cuadrados")
    habitaciones = models.IntegerField(default=0)
    baños = models.IntegerField(default=0)
    estacionamientos = models.IntegerField(default=0)
    
    # Estado y fechas
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Información adicional
    imagen = models.ImageField(upload_to='propiedades/', blank=True, null=True)
    destacada = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.tipo.nombre}"
