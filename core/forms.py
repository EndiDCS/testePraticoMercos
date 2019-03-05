from django import forms
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

class ClientForm(forms.Form):
    #Primeiro valor é o valor que sera usado o segundo da tupla e o que sera visto pelo usuario
    clientes = forms.ChoiceField(choices = CLIENT_CHOICES)
class ItemForm(forms.Form):
    #Primeiro valor é o valor que sera usado o segundo da tupla e o que sera visto pelo usuario                      
    produtos = forms.ChoiceField(choices = PRODUCT_CHOICES)
    quantidade = forms.IntegerField(min_value=0)
    preco = forms.FloatField(min_value=0)

