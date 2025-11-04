<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    

    <?php
    

     //Verifica se o formulário foi enviado via POST
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $nomeCli = $_POST["nomeCliente"];
        $tel = $_POST["telefone"];
        $data = $_POST["dataAtendimento"];
        $descricao = $_POST["descricaoProblema"];

        if(!empty($_POST["outroAparelho"])) {
        $aparelho = $_POST["outroAparelho"];
        } else {
        $aparelho = $_POST["aparelhoSelecionado"];
        }
        

        //Conexão com o Banco de Dados
        
        $conn = new mysqli("localhost", "root", "aluno", "assistenciadv", "3307");

        if($conn->connect_error){
            die("<p style='color:red;'>Erro na conexão com o banco de dados: " . $conn->connect_error . "</p>");
        }

        // inserir os Dados
        
        $sql = "INSERT INTO agendamentos (nome, telefone, aparelho, dat, descricao)
                VALUES ('$nomeCli', '$tel', '$aparelho', '$data', '$descricao')";


        if ($conn->query($sql) === TRUE){
        } else{
            echo "<p style+'color:red;'> ❌ Erro ao salvar: " . $conn->error . "</p>";
        }

        $conn->close();
    }
     //Verifica se o formulário foi enviado via POST
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $nomeCli = $_POST["nomeCliente"];
        $tel = $_POST["telefone"];
        $data = $_POST["dataAtendimento"];
        $descricao = $_POST["descricaoProblema"];

    
    
            
            echo "<div class='resultado'>";
            echo "<h1 id='h'>Dados do Agendamento:</h1>";
            echo "<p><strong>Nome:</strong> $nomeCli</p>";
            echo "<p><strong>Telefone:</strong> $tel</p>";
            echo "<p><strong>Aparelho:</strong> $aparelho</p>";
            echo "<p><strong>Data:</strong> $data</p>";
            echo "<p><strong>Descrição do problema:</strong> $descricao</p>";
            
    
            echo "<br>";
            echo "<br>";
            echo "<a href='form.php'>Voltar</a>";
            echo "</div>";
    }
    ?>
        
</body>
</html>