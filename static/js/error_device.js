$(document).ready(function () {


    $('.btn-abrir,.btn-deletar').click(function () {


        
        var itemId = $(this).data('item-id');
        var minhaDiv = document.getElementById('divItem' + itemId);
        console.log(minhaDiv)
        console.log(itemId)
        $.ajax({
            url: '/sending/' + itemId + '/',  // Substitua com a URL correta da sua view
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                
              
                var data_views = data.sua_variavel
                var error_div = document.getElementById(data_views +'_div_' + itemId);
                console.log(data_views);
                console.log(error_div);
                if(data_views === true){
                    window.location.reload();
                    console.log('executando.............')
                }else{
                
                minhaDiv.classList.remove('escondido');
                minhaDiv.classList.add('visivel');
                error_div.classList.remove('escondido');
                error_div.classList.add('visivel');
                }
                console.log("funcionando");
                console.log(minhastring);



            },
            error: function (error) {
                
                console.log('Erro ao obter a variável:', error);


            }

        });

    });
});

