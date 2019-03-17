from django.db import models
from django.forms import NumberInput

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)

class Item(models.Model):
    quantidade_digitada_pelo_usuario = models.IntegerField(default=1)
    preco_digitado_pelo_usuario = models.FloatField(default = 550000.00)
    produto = models.CharField(max_length=100)
    rentabilidade = models.CharField(max_length=100,null=True)
    referencia_pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)

