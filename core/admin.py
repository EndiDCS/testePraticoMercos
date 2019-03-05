from django.contrib import admin
from .models import Cliente,Produto,Item,Pedido,Order
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Pedido)
admin.site.register(Order)