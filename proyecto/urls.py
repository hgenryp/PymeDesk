from django.urls import include, path
from .views import ClienteList, ClienteDetail, PedidoList, PedidoDetail, ProductoList, ProductoDetail

urlpatterns = [
    path('cliente/', ClienteList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>', ClienteDetail.as_view(), name='cliente-detail'),
    
    path('producto/', ProductoList.as_view(), name='producto-list'),
    path('producto/<int:pk>', ProductoDetail.as_view(), name='producto-detail'),
    
    path('pedido/', PedidoList.as_view(), name='pedido-list'),
    path('pedido/<int:pk>', PedidoDetail.as_view(), name='pedido-detail'),
    
]