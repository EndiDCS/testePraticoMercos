from django import forms

class PedidoForm(forms.Form):
    #Primeiro valor é o valor que sera usado o segundo da tupla e o que sera visto pelo usuario
    #Clientes Pré Cadastrados
    CLIENT_CHOICES = ((1,'Darth​ ​Vader'),
                     (2,'Obi-Wan​ ​Kenobi'),
                     (3,'Luke​ ​Skywalker'),
                     (4,'Imperador​ ​Palpatine'),
                     (5,'Han​ ​Solo'))
    #Produtos Pré Cadastrados                 
    PRODUCT_CHOICES = ((1,'Millenium​ ​Falcon'),
                     (2,'X-Wing'),
                     (3,'Super​ ​Star​ ​Destroyer'),
                     (4,'TIE​ ​Fighter'),
                     (5,'Lightsaber'),
                     (6,'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle'),
                     (7,'DL-44​ ​Heavy​ ​Blaster​ ​Pistol'))                  
    clientes = forms.ChoiceField(choices = CLIENT_CHOICES)
    produtos = forms.ChoiceField(choices = PRODUCT_CHOICES)
    quantidade = forms.IntegerField(min_value=0)
    preco = forms.FloatField(min_value=0)

