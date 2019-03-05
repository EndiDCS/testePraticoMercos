from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PedidoForm
from .models import Item

#constantes
from .constantes import endi

# Create your views here.
#renderiza a página inicial
def index(request):
    return render(request,'core/index.html')

#trata o novo pedido
def novoPedido(request):
    #se a requisição chega com o verbo POST processa os dados recebidos e realiza as operações necessárias
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            #processa os dados do formulario  e redireciona para alguma url
            client = form.cleaned_data['clientes']
            product = form.cleaned_data['produtos']
            quantity = form.cleaned_data['quantidade']
            price = form.cleaned_data['preco']
            eu = endi['daniel']
            #daqui pra baix realizar operacoes com os dados obtidos pelo formulario
            #criar o item no banco de dados
            #i = Item(quantidade_digitada_pelo_usuario=quantity,preco_digitado_pelo_usuario=price,)
            #antes de salvar o item realizar as validações
            
            context = {'client':client,'product':product,'quantity':quantity,'price':price,'eu':eu}
            return render(request,'core/resultado.html',context)
    else:
        #caso a requisição não chegue como POST renderiza o formulario no formto padrão para o usuário
        form = PedidoForm()
    return render(request,'core/novoPedido.html',{'form':form})

def resultadoPedido(request):
    return render(request,'core/resultado.html')    