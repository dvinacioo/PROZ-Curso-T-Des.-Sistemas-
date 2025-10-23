<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Black Sexta</title>
</head>
<body>

    <?php
    //Verifica se o formulário foi enviado via POST
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $nome = $_POST["nomeProduto"];
        $categoria = $_POST["categoria"];
        $preco = $_POST["precoProduto"];
        $estoque = $_POST["qntdEstoque"];

        echo "<h3> Produtos Cadastrados (POST)</h3>";
        echo "Produto: $nome<br>";
        echo "Categoria: $categoria<br>";
        echo "Preço R$ $preco<br>";
        echo "Qntd em Estoque: $estoque <br>";
    }
    if(isset($_GET['campanha']) && isset($_GET['versao'])){
        $campanha = $_GET['campanha'];
        $versao = $_GET['versao'];


        echo "<br> <br> Capanha: $campanha<br>";
        echo "Versão: $versao";
    }
    ?>
</body>
</html>