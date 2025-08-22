
function verifica(){
    let nomes = ["Davi", "Lucas", "Luzia"];
    let senhas =["123", "1234", "12345"];

    const mensagem = document.getElementById("msg");
    const nameInput = document.getElementById("username");
    const senhaInput = document.getElementById("senha");
    
    const name = nameInput.value;
    const acesso = senhaInput.value;

    let correto = false;

    for(let i = 0; i < nomes.length; i++){
        if(name === nomes[i] && acesso === senhas[i]){
            correto = true;
            setTimeout(() => {
                mensagem.innerHTML = "Será que você está cadastrado?";
                mensagem.style.color = "blue" 
                nameInput.value = '';
                senhaInput.value = '';
        }, 5000)
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
