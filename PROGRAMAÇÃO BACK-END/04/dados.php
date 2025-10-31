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