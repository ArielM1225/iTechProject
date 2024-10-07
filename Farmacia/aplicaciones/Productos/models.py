from django.db import models
from aplicaciones.Movimientos.models import Entrada, EntradaProducto
from aplicaciones.Movimientos.models import Salida, SalidaProducto



class Producto (models.Model):
    
    tipo_choice = (
        ('venta libre', 'Venta Libre'),
        ('bajo receta', 'Bajo Receta'),
        ('bajo receta duplicada', 'Bajo receta duplicado-Lista IV'),
    )
    
    id_producto= models.AutoField(primary_key=True)
    nombre_Comercial=models.CharField ('Nombre',max_length=17)
    id_Laboratorio = models.ForeignKey('Comunidad.Laboratorio', on_delete=models.CASCADE, verbose_name= 'Laboratorio')
    principio_activo=models.CharField ('Droga',max_length=17)
    presentacion=models.CharField ('Presentacion',max_length=17)
    tipo_Producto=models.CharField(choices=tipo_choice, max_length=45, verbose_name='Tipo de producto')
    accion_farma=models.CharField ('Acción',max_length=17)
    stock = models.PositiveBigIntegerField(default=0) # Campo de stock, no permite valores negativos
    
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural='Medicamentos'
        unique_together=('nombre_Comercial','principio_activo','presentacion')
    
    def __str__(self):
        return self.nombre_Comercial
    

    

    
    


