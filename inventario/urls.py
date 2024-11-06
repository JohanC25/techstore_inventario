# inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('<int:pk>/agregar_stock/', views.agregar_stock, name='agregar_stock'),
    path('<int:pk>/detalle/', views.detalle_producto, name='detalle_producto'),
]
