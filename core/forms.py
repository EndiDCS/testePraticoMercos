from django import forms
from django.forms import ModelForm,Select
from .models import Pedido,Item
from django.forms import Select
from decimal import Decimal
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

PRECO_PRODUTOS = {
    'Millenium​ ​Falcon':550000,
    'X-Wing':60000,
    'Super​ ​Star​ ​Destroyer':4570000,
    'TIE​ ​Fighter':75000,
    'Lightsaber':6000,
    'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle':5800,
    'DL-44​ ​Heavy​ ​Blaster​ ​Pistol':1500
    }

MULTIPLO_PRODUTOS = {
    'Millenium​ ​Falcon':0,
    'X-Wing':2,
    'Super​ ​Star​ ​Destroyer':0,
    'TIE​ ​Fighter':2,
    'Lightsaber':5,
    'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle':0,
    'DL-44​ ​Heavy​ ​Blaster​ ​Pistol':10
    }                      

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
        labels = {'quantidade_digitadada_pelo_usuario':'Quantidade','preco_digitado_pelo_usuario':'Preço'}


    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantidade_digitadada_pelo_usuario")
        product = cleaned_data.get("produto")
        price = cleaned_data.get("preco_digitado_pelo_usuario")
        multiplo = MULTIPLO_PRODUTOS[product]
        error1 = False
        error2 = False
        error3 = False

        if(MULTIPLO_PRODUTOS[product] != 0):
            if((quantity % multiplo) != 0 ):
                error1 = True
                #raise forms.ValidationError("Quantidade não é multipla")

        if(price < (PRECO_PRODUTOS[product] - (PRECO_PRODUTOS[product]*0.1) )):      
            error2=True
            #raise forms.ValidationError("Rentabilidade Ruim")

        if(quantity <= 0):
            error3=True

        if(error1 and error2 and error3):
            raise forms.ValidationError([
                forms.ValidationError(('|Este produto precisa ser multiplo de %s|' % multiplo), code='error1'),
                forms.ValidationError(('|Rentabilidade Ruim|'), code='error2'),
                forms.ValidationError(('|Quantidade precisa ser maior do que zero|'), code='error3'),
            ])        
        if(error1 and error2):        
           raise forms.ValidationError([
                forms.ValidationError(('|Este produto precisa ser multiplo de %s|' % multiplo), code='error1'),
                forms.ValidationError(('|Rentabilidade Ruim|'), code='error2'),
            ])     
        if(error1 and error3):        
            raise forms.ValidationError([
                forms.ValidationError(('|Este produto precisa ser multiplo de %s|' % multiplo), code='error1'),
                forms.ValidationError(('|Quantidade precisa ser maior do que zero|'), code='error3'),
            ])     
        if (error2 and error3):
            raise forms.ValidationError([
                forms.ValidationError(('|Rentabilidade Ruim|'), code='error2'),
                forms.ValidationError(('|Quantidade precisa ser maior do que zero|'), code='error3'),
            ])     
        if(error1):  
            raise forms.ValidationError("Quantidade não é multipla ou é menor ou igual a Zero")
        if (error2 and error3):
            raise forms.ValidationError("Rentabilidade Ruim")            
        if (error3):
            raise forms.ValidationError("Quantidade precisa ser maior do que zero")    
       
    



