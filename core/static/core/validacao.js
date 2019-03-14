
    const preco_produtos = {
        'Millenium​ ​Falcon':550000,
        'X-Wing':60000,
        'Super​ ​Star​ ​Destroyer':4570000,
        'TIE​ ​Fighter':75000,
        'Lightsaber':6000,
        'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle':5800,
        'DL-44​ ​Heavy​ ​Blaster​ ​Pistol':1500
    }

    $(document).ready(function() {
        $('#id_produto').change(function () {
            // url da view responsvel por calcular o novo preço
            var url = $("#pedidoForm").attr("muda_preco_url"); 
            // novo produto selecionado pelo usuario
            var produto = $(this).val();  
           // console.log(preco_produtos[produto])
            $.ajax({                       
                url: url, //url da view
                data: {
                    'produto': produto  //informa a view qual o novo produto escolhido pelo usuario
                },            
                success: function (preco) {   // preco é o retorno da função implementada nas views, logo o novo preço que será mostrado ao usuário
                    $('input[name="preco_digitado_pelo_usuario"]').val(preco);
                    $('#rentabilidade').html('Rentabilidade boa')
                    $('#rentabilidade').css('color','green')
                }
            });
        });

        $('input[name="preco_digitado_pelo_usuario"]').keyup(function(){
            var preco = $(this).val();
            var produto = $('#id_produto').val()
            console.log(preco_produtos[produto])
            
            
           // verifica a rentabilidade se for ruim avisa ao usuário
            if(preco < (preco_produtos[produto] - (preco_produtos[produto]*0.1) )){
                console.log('ruim')
                $('#rentabilidade').html('Rentabilidade ruim')
                $('#rentabilidade').css('color','red')
            } else if (preco > preco_produtos[produto]){
                console.log('otimo')
                $('#rentabilidade').html('Rentabilidade ótima')
                $('#rentabilidade').css('color','green')
            } else {
                console.log('boa')
                $('#rentabilidade').html('Rentabilidade boa')
                $('#rentabilidade').css('color','green')
            }    
            //dica para mim mesmo, ao mudar o produto mudar a rentabilidade para boa
            //ao cliclar em submite rentabilidade mesmo estando ruim vai para boa mudar isso
            
        });

    });
