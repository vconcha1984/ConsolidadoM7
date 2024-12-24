from django.db import models
from django.core.validators import MinValueValidator
import datetime

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, null=True)
    pais   = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.laboratorio}'
    
    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[MinValueValidator(datetime.date(2015,1,1))])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Validar los campos de la tabla antes de Guardar
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f'{self.nombre} - {self.laboratorio}'