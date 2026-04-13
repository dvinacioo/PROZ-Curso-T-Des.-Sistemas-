function mostrarDados(){
        let nome = document.getElementById("nomeUser").value;
        let idade = document.getElementById("idadeUser").value;
        let sexo = document.getElementById("sexoUser").value;
        let pressao = document.getElementById("pressaoUser").value;
        let temperatura = document.getElementById("temperaturaUser").value;
        let frequencia = document.getElementById("frequenciaUser").value;
        let saturacao = document.getElementById("saturacaoUser").value;
        let evolucao = document.getElementById("evolucaoUser").value;
        let medicamento = document.getElementById("medicamentoUser").value;
        let dosagem = document.getElementById("dosagemUser").value;
        let horario = document.getElementById("horarioUser").value;
        
        let resultado = `
        <ul class="list-group">
           <li class="list-group-item"><strong>Nome:</strong> ${nome} <br> </li>
           <li class="list-group-item"><strong>Idade:</strong> ${idade} <br> </li>
           <li class="list-group-item"><strong>Sexo:</strong> ${sexo} <br> </li>
           <li class="list-group-item"><strong>Pressão Arterial:</strong> ${pressao} <br> </li>
           <li class="list-group-item"><strong>Temperatura:</strong> ${temperatura} <br> </li>
           <li class="list-group-item"><strong>Frequência Cardiaca:</strong> ${frequencia} <br> </li>
           <li class="list-group-item"><strong>Saturação:</strong> ${saturacao} <br> </li>
           <li class="list-group-item"><strong>Evolução:</strong> ${evolucao} <br> </li>
           <li class="list-group-item"><strong>Medicamento:</strong> ${medicamento} <br> </li>
           <li class="list-group-item"><strong>Dosagem:</strong> ${dosagem} <br> </li>
           <li class="list-group-item"><strong>Horário:</strong> ${horario} </li>
        `;
        
        
        let caixa = document.getElementById("resultado");
        caixa.querySelector(".card-body").innerHTML = resultado;
        caixa.classList.remove("d-none");


        let toast = new bootstrap.Toast(document.getElementById('toastSucesso'));
        toast.show();


        document.querySelector("form").reset();
        }

        