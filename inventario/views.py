from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Inventario
from .forms import ProductoForm, InventarioForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})

def agregar_stock(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    inventario = get_object_or_404(Inventario, producto=producto)  # Buscar el inventario asociado al producto
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 0))
        inventario.cantidad_disponible += cantidad
        inventario.save()
        return redirect('lista_productos')
    return render(request, 'inventario/agregar_stock.html', {'inventario': inventario, 'producto': producto})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})