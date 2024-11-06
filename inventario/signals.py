from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto, Inventario

@receiver(post_save, sender=Producto)
def crear_inventario(sender, instance, created, **kwargs):
    if created:
        # Si se crea un nuevo producto, creamos su inventario con stock inicial 0
        Inventario.objects.create(
            producto=instance,
            cantidad_disponible=0,
            ubicacion_tienda="Principal",
            estado_stock="Disponible"
        )
