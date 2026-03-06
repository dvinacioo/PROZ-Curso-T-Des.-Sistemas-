const user = ["admin","davi", "dev", "time"]
const senhas = ["1234", "21042007", "junior", "cruzeiro"]


function validar(){
    const name = document.getElementById("user").value;
    const password = document.getElementById("password").value;

    let correto = false;

    for(let i = 0; i < user.length; i++){
        if(name === user[i] && password === senhas[i]){
            correto = true;
            break;
            
        }
    }
        if(correto){
            // salva o usuário
            localStorage.setItem("usuarioLogado", name);
            window.location.href = "pagina.html";
            return;   
        } else{
            window.alert("Dados incoretos. Tente novamente!");
        }
    
}