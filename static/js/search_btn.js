$(document).ready(function () {

    function myFunction() {
        $("#button_search").hide();
        $("#loading").show();
        var chave1_mac = $("#input_chave1").val();
       
        console.log(chave1_mac)
        var dados = {
            "chave1": chave1_mac,
            
            
        };
        $.ajax({
            url: '/confirm/', // URL da sua view Django que processará a confirmação
            type: 'POST',       // Método HTTP, neste caso é um pedido GET
            data: JSON.stringify(dados),
            contentType: 'application/json',
           
            success: function (data) {
                var data_views = data.confirmation
                console.log(data_views)
                if (data_views === true) {
                    
                    $("#loading").hide();
                    $("#founded_device").show();
                    $("#input_chave1").hide();
                    $("#label_chave1").hide();
                    $("#founded_device2").show();
                } else {
                    // Lógica para o caso em que a confirmação não foi recebida
                    $("#loading").hide();
                    $("#"+data_views).show();

                    $("#button_search2").show();
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