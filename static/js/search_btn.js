$(document).ready(function () {

    function myFunction() {
        $("#button_search").hide();
        $("#loading").show();
        var chave1 = $("#input_chave1").val();
        var chave2 = $("#input_chave2").val();
        console.log(chave1,chave2)
        var dados = {
            chave1: chave1,
            chave2: chave2,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        };
        $.ajax({
            url: '/confirm/', // URL da sua view Django que processará a confirmação
            type: 'POST',       // Método HTTP, neste caso é um pedido GET
            data: JSON.stringify(dados),
            contentType: 'application/json',
            success: function (data) {
                console.log(data.confirmation)
                console.log("deu certo")
            },
            error: function (xhr, status, error) {
                // Função chamada em caso de erro na requisição
                console.error("Erro na requisição AJAX:", status, error);
                // Se ocorrer um erro, você pode ocultar #loading aqui se necessário
            }
        });
    }

    // Vincula a função ao evento de clique do botão
    $('#button_search').on('click', function () {
        myFunction();
    });
});