$(document).ready(function () {
    $("#button_search").click(function () {
        $("#button_search").hide();
        $("#loading").show();
        $.ajax({
            url: '/confirm/', // URL da sua view Django que processará a confirmação
            type: 'GET',       // Método HTTP, neste caso é um pedido GET
            success: function (data) {
                // Função chamada em caso de sucesso na requisição
                if (data.confirmation) {
                    // Supondo que a confirmação foi recebida com sucesso.
                    $("#button_search").show();
                    $("#loading").hide();
                } else {
                    // Lógica para o caso em que a confirmação não foi recebida
                    console.error("Falha na confirmação.");
                    // Se desejar, você pode ocultar #loading aqui também
                }
            },
            error: function (xhr, status, error) {
                // Função chamada em caso de erro na requisição
                console.error("Erro na requisição AJAX:", status, error);
                // Se ocorrer um erro, você pode ocultar #loading aqui se necessário
            }
        });
    });
});