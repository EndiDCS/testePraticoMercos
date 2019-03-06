from django import forms
from django.forms import ModelForm,Select
from .models import Pedido,Item
from django.forms import Select
#Primeiro valor é o valor que sera usado o segundo da tupla e o que sera visto pelo usuario
#Clientes Pré Cadastrados
CLIENT_CHOICES = (('Darth​ ​Vader','Darth​ ​Vader'),
                     ('Obi-Wan​ ​Kenobi','Obi-Wan​ ​Kenobi'),
                     ('Luke​ ​Skywalker','Luke​ ​Skywalker'),
                     ('Imperador​ ​Palpatine','Imperador​ ​Palpatine'),
                     ('Han​ ​Solo','Han​ ​Solo'))
#Produtos Pré Cadastrados
PRODUCT_CHOICES = (('Millenium​ ​Falcon','Millenium​ ​Falcon'),
                     ('X-Wing','X-Wing'),
                     ('Super​ ​Star​ ​Destroyer','Super​ ​Star​ ​Destroyer'),
                     ('TIE​ ​Fighter','TIE​ ​Fighter'),
                     ('Lightsaber','Lightsaber'),
                     ('DLT-19​ ​Heavy​ ​Blaster​ ​Rifle','DLT-19​ ​Heavy​ ​Blaster​ ​Rifle'),
                     ('DL-44​ ​Heavy​ ​Blaster​ ​Pistol','DL-44​ ​Heavy​ ​Blaster​ ​Pistol'))

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente']
        widgets = {'cliente': Select(choices=CLIENT_CHOICES)}

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['produto','quantidade_digitadada_pelo_usuario','preco_digitado_pelo_usuario']   
        widgets = {'produto': Select(choices=PRODUCT_CHOICES)} 



