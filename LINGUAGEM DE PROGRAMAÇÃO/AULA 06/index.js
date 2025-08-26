function mensagem() {
    const usarios = [
        {login: "Laura", senha:"1234"},
        {login: "Carlos", senha:"abcd"},
        {login:"Mariana", senha:"5678"}
    ]

    const loginDigitado = document.getElementById("Login").value;
    const senhaDigitada = document.getElementById("senha").value;
    const mensagem = document.getElementById("mensagem");
    let encontrado = false;

    for(let i = 0; i <= usarios.length; i++){
        if(login === usarios[i].login && senha === usuarios[i].senha){
            encontrado = true;
            mensagem.innerHTML = "Bem-vindo, " + usuarios[i].login + "!";
        }
    }

    if(!encontrado){
        mensagem.innerHTML = "Login ou senha incorretas"
    }
}