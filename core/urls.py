from django.urls import path
from .views import index,novoPedido,editaPedido,todosPedidos,muda_preco,delete_item,delete_pedido

app_name = 'core'
urlpatterns = [
    path('',index,name='index'),
    path('pedido',novoPedido,name='formularioPedido'),
    path('edita/<int:id>/<int:id2>/',editaPedido,name='editaPedido'),
    path('deleta/<int:id>/',delete_item,name='deleteItem'),
    path('deletap/<int:id>/',delete_pedido,name='deletePedido'),
    path('produtos',todosPedidos,name='todosPedidos'),
    path('ajax/muda-preco/',muda_preco, name='ajax_muda_preco'),
]