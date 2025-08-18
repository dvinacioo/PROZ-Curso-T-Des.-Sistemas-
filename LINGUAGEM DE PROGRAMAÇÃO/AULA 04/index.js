function verficaPalavra(){
    let palavras = ["Sol", "Lua", "Estrela"];
    const input = document.getElementById("palavra").value;
    const mensagem = document.getElementById("mensagem");
    let encontrado = false; //começa com false

    //Percorre o array para verificar se a palavra está presente
    for(let i = 0; i < palavras.length; i++){
        if(input === palavras[i]){
            encontrado = true; //altera para true
            mensagem.innerHTML = "Você digitou uma palavra cadastrada"
        }
    }
    if(!encontrado){
        mensagem.innerHTML = "Palavra não cadastrada"
    }
}