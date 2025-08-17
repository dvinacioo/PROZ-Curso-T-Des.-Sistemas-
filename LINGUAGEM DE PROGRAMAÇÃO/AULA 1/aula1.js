//Função executada quando o butão é clicado
function mudarMensagem() { 
    const men = document.getElementById("mensagem");//Cria a função 'men' que busca o elemento "mensagem" no HTML 

    men.innerHTML = "Você acabou de GANHAR 10% de descontos em todos os produtos da loja! <br> Aproveite!" // faz que a função 'men' altera a mensagem do HTML
}