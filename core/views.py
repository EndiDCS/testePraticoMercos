from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ClientForm,ItemForm
from .models import Item,Order

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
            #product = request.POST.get('produtos')
            quantity = form2.cleaned_data['quantidade']
            price = form2.cleaned_data['preco']
            lista_acumulada = request.session.get('lista_acumulada')
            
           
            # se o usuário clicar no botão salvar, salva os dados no banco
            if('Salvar' in request.POST):
                #adiciona item na lista e salva no banco de dados
                lista=[product,quantity,price]
                lista_acumulada.append(lista)
                objeto = Order.objects.create(cliente = client, item = lista_acumulada)
                objeto.save()
                todos_objetos = Order.objects.all()
                context = {'lista_acumulada':objeto.item,'todos':todos_objetos}
                return render(request,'core/resultado.html',context)
                
            #se o usuário clicar no botão para adicionar um novo item    
            if('Adicionar' in request.POST):
                form2=ItemForm()

                #adiciona item a lista e salva na seção
                lista=[product,quantity,price]
                lista_acumulada.append(lista)
                request.session['lista_acumulada'] = lista_acumulada
                
                return render(request,'core/novoPedido.html',{'form1':form1,'form2':form2})
            
    else:
        #caso a requisição não chegue como POST renderiza o formulario no formato padrão para o usuário
        #se cancelar volta pra página inicial
        if('Cancelar' in request.GET):
            return HttpResponseRedirect(reverse('core:index'))
        #instancia os formulários vazios para que o usuário possa preencher
        form1 = ClientForm()
        form2 = ItemForm()
        lista_acumulada=Order(cliente = 'client', item = [])
        lista = lista_acumulada.item
        request.session['lista_acumulada'] =lista
    return render(request,'core/novoPedido.html',{'form1':form1,'form2':form2})

def resultadoPedido(request):
    return render(request,'core/resultado.html')    