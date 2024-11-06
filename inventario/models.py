from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='inventario')
    cantidad_disponible = models.IntegerField()
    ubicacion_tienda = models.CharField(max_length=255)
    estado_stock = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.producto.nombre} - {self.ubicacion_tienda}'
