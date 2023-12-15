$(document).ready(function () {
    
    function myFunction() {
        $("#button_search2").hide();
        $("#conflited_mac").hide();
        $("#JSON_invalid").hide();
        $("#time_over").hide();
        $("#Broken_msg").hide();
        $("#loading").show();
       
        $.ajax({
            url: '/confirm/', // URL da sua view Django que processará a confirmação
            type: 'GET',       // Método HTTP, neste caso é um pedido GET
            success: function (data) {
                console.log(data.confirmation)
                var data_views = data.confirmation
                if (data_views === true) {
                    console.log('????????')
                    $("#loading").hide();
                    $("#founded_device").show();
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
    $('.button_search2').on('click', function () {
        myFunction();
    });
});