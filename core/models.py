from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_cliente

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    preco_produto = models.FloatField(default=0.0)
    multiplo = models.IntegerField(default=0)
    def __str__(self):
        return self.nome_produto

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
#um item pode pertencer 
class Item(models.Model):
    quantidade_digitadada_pelo_usuario = models.IntegerField(default=0)
    preco_digitado_pelo_usuario = models.FloatField(default=0.0)
    referencia_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    referencia_produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    referencia_pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)


    