from django.db import models

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
#um item pode pertencer 
class Item(models.Model):
    quantidade_digitadada_pelo_usuario = models.IntegerField(default=0)
    preco_digitado_pelo_usuario = models.FloatField(default=0.0)
    produto = models.CharField(max_length=100)
    referencia_pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)

