from django.db import models

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
#um item pode pertencer 
class Item(models.Model):
    quantidade_digitadada_pelo_usuario = models.IntegerField(default=1)
    preco_digitado_pelo_usuario = models.DecimalField(default=550000,max_digits=10,decimal_places=2)
    produto = models.CharField(max_length=100)
    rentabilidade = models.CharField(max_length=100,null=True)
    referencia_pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)

