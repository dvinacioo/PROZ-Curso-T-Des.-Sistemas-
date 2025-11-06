<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CPF</title>
</head>
<body>
    <h2>Ssitema de login com CPF </h2>
    <form method="POST">
        <label>Digite seu CPF (apenas números):</label>
        <input type="text" name="cpf" minLength="11" maxlength="11" placeholder="Apenas 11 dígitos" required>
        <br><br>
        <input type="submit" name="cadastrar" value="Cadastrar  CPF">

    </form>
    <hr>

    <?php
    // Verifica se o formulário foi enviado via método POST
    if ($_SERVER["REQUEST_METHOD"] == "POST")   {

        // Captura o valor digitando no campo de CPF
        $cpf = $_POST["cpf"];

        // Verifica se o CPF contém apenas números e se possui exatamente 11 dígitos
        if(!ctype_digit($cpf) || strlen($cpf) != 11){
            // Mostra mensagem de erro e interrompe o código
            echo "<p>⚠️ O CPF deve conter exatamente 11 números.</p>";
            exit;
        }

        // Faz a conexão com o banco de dados MySQL
        // Parâmetros: servidor, usuário, senha, nome do banco e porta
        $conn = new mysqli("localhost", "root", "aluno", "recebecpf", "3307");
        
        // Verifica se houve erro na conexão
        if($conn->connect_error){
            // Se houve erro, encerra o script e mostra mensagem
        die("<p>Erro ao conectar: " . $conn->connect_error . "</p>");
        }

        // Se usuário clicou em "CADASTRAR"
        if(isset($_POST["cadastrar"])){
            // cria o comando SQL para inserir o CPF na tabela "usuarios"
            $sql = "INSERT INTO cliente (cpf) VALUES ('$cpf')";

            //Executa o comando e verifica se deu certo
            if($conn->query($sql) === TRUE){
                echo "<p>✅ CPF CADASTRADO COM SUCESSO!</p>";
            } else{
                // Caso o CPF já exista (chave primária repetida), exibe aviso
                echo "<p>⚠️ CPF já cadastrado.</p>";
            }
        }

        // Fecha a conexão com o banco
        $conn->close();
    }
    ?>
</body>
</html>