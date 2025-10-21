<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Formulário Outubro Rosa🩷</h2>
    <form action="index.php" method="post">
        <label>Nome:</label><br>
        <input type="text" name="nome" required><br><br>
        <label>Email:</label><br>
        <input type="email" name="email" required><br>
        <label>Idade:</label><br>
        <input type="number" name="idade" required><br><br>
        <label>Já realizou o exame de mamografia este ano?</label><br>
        <input type="radio" name="mamografia" value="Sim" required>Sim<br>
        <input type="radio" name="mamografia" value="Não">Não<br><br>
        <input type="submit" value="Enviar">
    </form>

    <?php
    //Verifica se o formulário foi enviado via POST
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $nome = $_POST["nome"];
        $mamografia = $_POST["mamografia"];
        $email = $_POST["email"];
        $idade = $_POST["idade"];

        echo "<h3>🩷 Dados Recebidos (POST)</h3>";
        echo "Nome: $nome<br>";
        echo "Idade: $idade<br>";
        echo "Email: $email<br>";
        echo "Fez mamorafia: $mamografia <br>";
        
    }
    ?>
</body>
</html>