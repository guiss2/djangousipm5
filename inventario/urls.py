from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import lista_clientes, lista_ventas, total_compras_cliente
from .views import nuevo_cliente
from .views import detalle_cliente
#esto e para los modelsviewset / creamos un router

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'ventas', views.VentaViewSet)
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact, name='contact'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/', views.productoFormView, name='productos'),
    path('', views.index, name='index'),
   
    path('categoria/', views.CategoriaCreateView.as_view(), name='categoria-create-list'),
    path('categorias/cantidad/', views.categoria_count, name='categoria-count'),
    path('productos/filtrar/unidades', views.productos_en_unidades, name='productos-unidades'),
    path('reporte/productos', views.reporte_productos, name='reporte-productos'),
    path('enviar/mensaje/', views.enviar_mensaje, name='enviar-mensaje'),
    path('total-compras/<int:cliente_id>/', total_compras_cliente, name='total_compras_cliente'),
   
   
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/<int:id>/', detalle_cliente, name='detalle_cliente'),
    path('clientes/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('ventas/', lista_ventas, name='lista_ventas'),
    path('ventas/<int:id>/', views.detalle_venta, name='detalle_venta'),
    path('ventas/nueva/', views.nueva_venta, name='nueva_venta'),

    
    
    path('', include(router.urls)),
]