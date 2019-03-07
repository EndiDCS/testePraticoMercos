from django.urls import path
from .views import index,novoPedido,resultadoPedido,editaPedido,todosPedidos,muda_preco

app_name = 'core'
urlpatterns = [
    path('',index,name='index'),
    path('pedido',novoPedido,name='formularioPedido'),
    path('resultado',resultadoPedido,name='resultadoPedido'),
    path('edita/<int:id>/<int:id2>/',editaPedido,name='editaPedido'),
    path('produtos',todosPedidos,name='todosPedidos'),
    path('ajax/muda-preco/',muda_preco, name='ajax_muda_preco'),
]