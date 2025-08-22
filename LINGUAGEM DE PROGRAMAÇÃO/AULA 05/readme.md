Nesta atividade nós teríamos que pegar nosso código feito no trabalho passado e adicionar uma função que limpasse os campos e voltasse com a Mensagem inicial.

O que foi feito é que agora possuo uma variavel para pegar o valor do Input ao invés de pega-lo diretamento do "ById". E também foi removido a função 'Break' que era desnecessária no código.
Código js Original:

"
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
"
