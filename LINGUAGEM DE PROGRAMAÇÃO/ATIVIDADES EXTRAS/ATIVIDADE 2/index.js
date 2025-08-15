function validaSenha(){
    const senha = "1234";
    const input = document.getElementById("campomsg");
    const valorDigitado = input.value;
    const but = document.getElementById("botao")

    if(valorDigitado === senha){
        input.value = "";
        input.placeholder = "Senha correta!";
        but.disabled = true;
    }
    else{
        input.value = "";
        input.placeholder = "Senha incorreta!"
    }
     input.blur();
}