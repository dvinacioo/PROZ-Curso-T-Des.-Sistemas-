const formulario = document.getElementById("formLogin");

formulario.addEventListener("submit", function(event){
    event.preventDefault();

const user = [
    {
        nome: "Davi Inácio",
        senha: "123456"
    }
];

let msg = document.getElementById("mensagem");


    let nome = document.getElementById("nome").value;
    let senha = document.getElementById("senha").value;

    for(let i = 0; i < user.length; i++){

        if(senha.length < 6){
            msg.innerHTML = "A senha precisa ter no mínimo 6 caracteres.";
            return;
        }

        else if(nome == user[i].nome && senha == user[i].senha){

            msg.innerHTML = "Login realizado com sucesso!";

            setTimeout(() => {
                window.location.href = "home.html";
            }, 2000);

            return;
        }
    }

    msg.innerHTML = "Nome ou senha incorretos.";

});