import { calcula,multiplo } from './calcula.js'; 
const calculaRentabilidade = calcula 
const calculaMultiplo = multiplo

const modificaDivMultiplo = function(){
    var multi = calculaMultiplo()
    if(multi > 0)
    {
        $("#quantidade").html(`Aviso: Este produto só pode ser vendido em quantidade multipla de ${multi}`)
    }else{
        $('#quantidade').html('')
    }
}
$(document).ready(function() {
    //para evitar inconsistências quando ocorre a atualização da página calcula-se o valor multiplo do produto
    modificaDivMultiplo()
    //quando o produto escolhido pelo usuário mudar, executar o código abaixo
    $('#id_produto').change(function () {
        // se o produto necessita ser vendido em quantidade multipla de um valor X então avisa ao usuário
        modificaDivMultiplo()
        //busca a url da view responsavel por buscar o novo preço do produto
        var url = $("#pedidoForm").attr("muda_preco_url"); 
        // novo produto selecionado pelo usuario
        var produto = $(this).val();  
        $.ajax({                       
            url: url, //url da view
            data: {
                'produto': produto  //informa a view qual o novo produto escolhido pelo usuario
            },            
            success: function (preco) {   // preco é o retorno da função muda_preco implementada nas views, logo o novo preço que será mostrado ao usuário
                $('input[name="preco_digitado_pelo_usuario"]').val(preco);
                // ao mudar de produto volta para a rentabilidade padrão 
                $('#rentabilidade').html('Rentabilidade boa')
                $('#rentabilidade').css('color','green')
            }
        });
    });
    // calcula a rentabilidade sempre que o usuário digitar uma tecla no campo de preço
    $('input[name="preco_digitado_pelo_usuario"]').keyup(function(){
        calculaRentabilidade();        
    });

});
