function verifica(){
    let nomes = ["Davi", "Lucas", "Luzia"];
    let senhas =["123", "1234", "12345"];

    const mensagem = document.getElementById("msg");
    const name = document.getElementById("username").value;
    const acesso = document.getElementById("senha").value;

    let correto = false;

    for(let i = 0; i < nomes.length; i++){
        if(name === nomes[i] && acesso === senhas[i]){
            correto = true;
            break;
        }
    }
    if(correto){
        mensagem.innerHTML = "Login Realizado com Sucesso!";
        mensagem.style.color = "green"
    } else{
        mensagem.innerHTML = "Digitação errada. Verificar Login e Senha!";
        mensagem.style.color = "red"
    }
}