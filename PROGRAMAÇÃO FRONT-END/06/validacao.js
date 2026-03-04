const user = [
        {
            "userName": "admin",
            "userPassord": "1234"
        }
        
    ]


function validar(){
    const name = document.getElementById("user").value;
    const password = document.getElementById("password").value;

    for(let i = 0; i < user.length; i++){
        if(name === user[i].userName && password === user[i].userPassord){
            window.location.href = "pagina.html";
            return;
        } else{
            window.alert("Dados incoretos. Tente novamente!");
        }
    }
}