from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ItemForm,PedidoForm
from .models import Item,Pedido
from django.shortcuts import get_object_or_404,redirect
#constantes
from .constantes import endi

#################funcoes para tratar e manipular os dados#################3


################# Views abaixo ################

#renderiza a página inicial
def index(request):
    p = Pedido.objects.all()
    i = Item.objects.all()
    return render(request,'core/index.html')

#trata o novo pedido
def novoPedido(request):
    #se a requisição chega com o verbo POST processa os dados recebidos e realiza as operações necessárias
    if request.method == 'POST':
        form1 = PedidoForm(request.POST)
        form2 = ItemForm(request.POST)
        if (form1.is_valid() & form2.is_valid()):
            #processa os dados do formulario  e redireciona para alguma url
            client = form1.cleaned_data['cliente']
            product = form2.cleaned_data['produto']
            quantity = form2.cleaned_data['quantidade_digitadada_pelo_usuario']
            price = form2.cleaned_data['preco_digitado_pelo_usuario']            
            #código old
            lista_acumulada = request.session.get('lista_acumulada')
            # se o usuário clicar no botão salvar, salva os dados no banco
            if('Salvar' in request.POST):
                #adiciona item na lista e salva no banco de dados
                lista=[product,quantity,price]
                lista_acumulada.append(lista)
                context = {'lista_acumulada':lista_acumulada,'client':client,'tamanho':len(lista_acumulada)}
                p = Pedido.objects.create(cliente=client)
                p.save()
                i=0
                listaDeItens=[]
                while (i < len(lista_acumulada)):
                    item = Item(quantidade_digitadada_pelo_usuario=lista_acumulada[i][1],
                    preco_digitado_pelo_usuario=lista_acumulada[i][2],
                    produto=lista_acumulada[i][0],
                    referencia_pedido=p)
                    item.save()
                    i = i + 1
                    listaDeItens.append(item)
                #i = Item.objects.all()   
                context = {'lista_acumulada':lista_acumulada,'client':client,'tamanho':len(lista_acumulada),'p':p,'item':listaDeItens}    
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
        form1 = PedidoForm()
        form2 = ItemForm()
        lista_acumulada=[]
        request.session['lista_acumulada'] =lista_acumulada
    return render(request,'core/novoPedido.html',{'form1':form1,'form2':form2})

def resultadoPedido(request):
    return render(request,'core/resultado.html')    

def editaPedido(request, id, id2): 
    instance = get_object_or_404(Pedido, id=id)
    formPedido = PedidoForm(request.POST or None, instance=instance)
    instance2 = get_object_or_404(Item, id=id2)
    formItem = ItemForm(request.POST or None, instance=instance2)
    if formPedido.is_valid() and formItem.is_valid():
        formPedido.save()
        formItem.save()
        return redirect('core:resultadoPedido')
    return render(request, 'core/editaPedido.html', {'formPedido': formPedido,'formItem':formItem})     