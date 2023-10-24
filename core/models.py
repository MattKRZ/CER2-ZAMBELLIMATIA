from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Entidades(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='core/upload_img')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"
    
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=200)
    detalle_corto = models.CharField(max_length=100)
    
    TIPO_CHOICES = [
        ("O", "Seleccionar una opción"),
        ("S", "Suspensión de actividades"),
        ("C", "Suspensión de clases"),
        ("I", "Información")
    ]

    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, default="O")
    entidad = models.ForeignKey(Entidades, on_delete=models.SET_NULL, null=True, blank=True)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True) # Actualiza DateTime al crear
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True) # Actualiza DateTime al modificar
    publicado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="publicado_por")
    modificado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="modificado_por")

    def __str__(self) -> str:
        return self.titulo
