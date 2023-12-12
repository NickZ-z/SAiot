$(document).ready(function () {
    var button_div = document.getElementById('button_search');
    function myFunction() {
        button_div.classList.remove('escondido');
        button_div.classList.add('visivel');
        $("#loading").show();
        
        $.ajax({
            url: '/confirm/', // URL da sua view Django que processará a confirmação
            type: 'GET',       // Método HTTP, neste caso é um pedido GET
            success: function (data) {
                console.log(data.confirmation);
                if (data.confirmation) {
                    
                    $("#loading").hide();
                    $("#founded_device").show();
                    $("#founded_device2").show();
                } else {
                    // Lógica para o caso em que a confirmação não foi recebida
                    $("#loading").hide();
                    $("#notfounded_device").show();
                    // Se desejar, você pode ocultar #loading aqui também
                }
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