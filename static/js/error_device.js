$(document).ready(function () {


    $('.btn-abrir,.btn-deletar').click(function () {


        var itemId = $(this).data('item-id');
       console.log(itemId)
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
                $('#divItem' + name).show();
            }

        });

    });
});
