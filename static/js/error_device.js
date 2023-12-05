$(document).ready(function () {
    // Quando qualquer botão é clicado
    $("#meu-botao").click(function () {
        // Obtém o ID do item associado ao botão clicado
        var itemId = $(this).data('item-id');

        // Chama a view do Django e obtém a variável
        $.ajax({
            url: '/sending/' + itemId + '/',  // Substitua com a URL correta da sua view
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                window.location.reload();
                if (data.sua_variavel) {
                    
                }
                console.log("funcionando")

              


            },
            error: function (error) {
                console.log('Erro ao obter a variável:', error);
                $('#divItem' + itemId).show();
            }

        });

    });
});