function mensagem() {
    const usuarios = [
        {login: "Davi", senha:"1234"},
        {login: "Lucas", senha:"abcd"},
        {login:"Thaina", senha:"5678"}
    ]

    const loginDigitado = document.getElementById("Login").value;
    const senhaDigitada = document.getElementById("senha").value;
    const mensagem = document.getElementById("mensagem");
    let encontrado = false;

    for(let i = 0; i < usuarios.length; i++){
        if(loginDigitado === usuarios[i].login && senhaDigitada === usuarios[i].senha){
            encontrado = true;
            mensagem.innerHTML = "Bem-vindo(a), " + usuarios[i].login + "!";

            // Aguarda 1.5seg e redireciona o usuário para outra página após validação.
            setTimeout(() => {
                mensagem.innerHTML = "Redirecionando...";
                window.location.href = "pagina2.html";
            },1500)
        }
    }
    if(!encontrado){
        mensagem.innerHTML = "Login ou senha incorretas. Tente novamente.";
        document.getElementById("Login").value = "";
        document.getElementById("senha").value = "";
    }
}