from django.urls import path
from .views import index,novoPedido,resultadoPedido

app_name = 'core'
urlpatterns = [
    path('',index,name='index'),
    path('pedido',novoPedido,name='formularioPedido'),
    path('resultado',resultadoPedido,name='resultadoPedido')
]