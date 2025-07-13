from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from inventario.serializers import CategoriaSerializer, ClienteSerializer, ContactSerializer, ProductoSerializer, ReporteProductosSerializer, VentaSerializer
from rest_framework import viewsets
from .models import Categoria, Cliente, Producto, Venta
from .forms import ProductoForm, VentaForm
from rest_framework import generics
from .forms import ClienteForm
from django.db.models import Sum
# Create your views here.
def index(request):
    return HttpResponse("Hola soy Maria Guisela Huanca Torrez")
#mis vistas de los modelos
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})
def nueva_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')  # Asegúrate de tener esta vista creada
    else:
        form = VentaForm()
    return render(request, 'form_ventas.html', {'form': form})

def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'venta_detalle.html', {'venta': venta})

def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'form_clientes.html', {'form': form})

def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'cliente_detalle.html', {'cliente': cliente})


def contact(request, name):
    return HttpResponse(f"Hello {name}, welcome.")
def categorias(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    # para filtrar las categorias Se recibe cun parametro con get
    filtro_nombre = request.GET.get("nombre")
    # import pdb; pdb.set_trace()
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        # Mostrar todas las categorías si no hay filtro
        categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {"categorias": categorias})


def productoFormView(request):
    form = ProductoForm()
    producto = None
    id_producto = request.GET.get("id")
    if id_producto:
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductoForm(instance=producto)
    if request.method == "POST":
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "form_productos.html", {"form": form})


# Controlador cremos la clase para el serializers
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# generic apiwiew


class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(["GET"])
def categoria_count(request):
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
@api_view(['GET'])
def productos_en_unidades(request ):
     try:
         productos = Producto.objects.filter(unidades='u')
         return JsonResponse(
             ProductoSerializer(productos, many=True).data,
             safe=False,
             status=200,
         )
     except Exception as e:
         return JsonResponse({'message': str(e)}, status=400)

@api_view(['GET'])
def reporte_productos(request):
    try:
        productos = Producto.objects.filter(unidades='u')
        cantidad = productos.count()
        return JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@api_view(['POST'])
def enviar_mensaje(request):
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({'message': 'Mensaje enviado correctamente'},
                            status=200)
    else:
        return JsonResponse({'message': cs.errors}, status=200)
    
    
@api_view(["GET"])
def total_compras_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        total = Venta.objects.filter(cliente=cliente).aggregate(total=Sum('monto'))['total'] or 0

        return JsonResponse(
            {
                "cliente": cliente.nombre,
                "total_compras": float(total)
            },
            status=200
        )
    except Cliente.DoesNotExist:
        return JsonResponse({"message": "Cliente no encontrado"}, status=404)

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)