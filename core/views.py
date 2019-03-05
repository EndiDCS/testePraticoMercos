from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ClientForm,ItemForm
from .models import Item

#constantes
from .constantes import endi

#################funcoes para tratar e manipular os dados#################3


################# Views abaixo ################

#renderiza a página inicial
def index(request):
    return render(request,'core/index.html')

#trata o novo pedido
def novoPedido(request):
    #se a requisição chega com o verbo POST processa os dados recebidos e realiza as operações necessárias
    if request.method == 'POST':
        
        form1 = ClientForm(request.POST)
        form2 = ItemForm(request.POST)
        if (form1.is_valid() & form2.is_valid()):
            
            

            #processa os dados do formulario  e redireciona para alguma url
            client = form1.cleaned_data['clientes']
            product = form2.cleaned_data['produtos']
            quantity = form2.cleaned_data['quantidade']
            price = form2.cleaned_data['preco']
            eu = endi['daniel']

            #daqui pra baix realizar operacoes com os dados obtidos pelo formulario
            #criar o item no banco de dados
            # = Item(quantidade_digitada_pelo_usuario=quantity,preco_digitado_pelo_usuario=price,)
            #antes de salvar o item realizar as validações
            
            context = {'client':client,'product':product,'quantity':quantity,'price':price,'eu':eu}
            return render(request,'core/resultado.html',context)
    else:
        #caso a requisição não chegue como POST renderiza o formulario no formto padrão para o usuário
        #se cancelar volta pra página inicial
        if('Cancelar' in request.GET):
            return HttpResponseRedirect(reverse('core:index'))
        form1 = ClientForm()
        form2 = ItemForm()
    return render(request,'core/novoPedido.html',{'form1':form1,'form2':form2})

def resultadoPedido(request):
    return render(request,'core/resultado.html')    