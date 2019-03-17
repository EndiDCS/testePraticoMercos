const preco_produtos = {
    'Millenium​ ​Falcon':550000,
    'X-Wing':60000,
    'Super​ ​Star​ ​Destroyer':4570000,
    'TIE​ ​Fighter':75000,
    'Lightsaber':6000,
    'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle':5800,
    'DL-44​ ​Heavy​ ​Blaster​ ​Pistol':1500
}

const multiplo_produtos = {
    'Millenium​ ​Falcon':0,
    'X-Wing':2,
    'Super​ ​Star​ ​Destroyer':0,
    'TIE​ ​Fighter':2,
    'Lightsaber':5,
    'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle':0,
    'DL-44​ ​Heavy​ ​Blaster​ ​Pistol':10
    }  
// função utilizada para calcular a rentabilidade do produto escolhido pelo usuário
export function calcula() {
    var preco = $('input[name="preco_digitado_pelo_usuario"]').val();
    var produto = $('#id_produto').val()
    // verifica a rentabilidade e avisa ao usuário
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
}

export function multiplo(){
    var produto = $('#id_produto').val()
    var valorMultiplo = multiplo_produtos[produto]
    return valorMultiplo
}
// essa função é chamada sempre que o usuário soltar uma tecla quando estiver digitando no campo de preços
export function fixaDuasCasas(){
    var valorNaoFormatado = $('input[name="preco_digitado_pelo_usuario"]').val()
    //verifica se o numero digitado possui casas decimais
    if(valorNaoFormatado.includes('.') ){
        //se possuir apenas uma ou duas casas decimais não faz nada
        if((valorNaoFormatado.charAt(valorNaoFormatado.length-2) == '.')){
            valorFormatado=valorNaoFormatado
            console.log('a')
        }//caso contrario apaga as casas decimais excedidas
        else{
            while(valorNaoFormatado.charAt(valorNaoFormatado.length-3) != '.'){   	
                valorNaoFormatado = valorNaoFormatado.substring(0,valorNaoFormatado.length-1);
            }
            console.log('b')
        }
    }
    var valorFormatado=valorNaoFormatado
    return valorFormatado   
}