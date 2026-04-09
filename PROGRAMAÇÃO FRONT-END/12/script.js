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
        <h5>Prontuário do Paciente</h5>
        Nome: ${nome} <br>
        Idade: ${idade} <br>
        Sexo: ${sexo} <br>
        Pressão Arterial: ${pressao} <br>
        Temperatura: ${temperatura} <br>
        Frequência Cardíaca: ${frequencia} <br>
        Saturação: ${saturacao} <br>
        Evolução: ${evolucao} <br>
        Medicamento: ${medicamento} <br>
        Dosagem: ${dosagem} <br>
        Horário: ${horario}
        `;
        
        
        let caixa = document.getElementById("resultado");
        caixa.innerHTML = resultado;
        caixa.classList.remove("d-none");


        let toast = new bootstrap.Toast(document.getElementById('toastSucesso'));
        toast.show();


        document.querySelector("form").reset();
        }

        