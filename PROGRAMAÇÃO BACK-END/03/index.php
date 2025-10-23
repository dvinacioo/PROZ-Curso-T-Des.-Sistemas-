<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Black Sexta</title>
</head>
<body>
    <h2>Cadastro de produtos</h2>
    <form action="produtos.php?campanha=black-friday&versao=1.1" method="post">
        <label>Nome do produto:</label><br>
        <input type="text" name="nomeProduto" required><br>
        <Label>Categoria:</Label> <br>
        <input type="radio" name="categoria" value="ALimentos" required> Alimentos <br>
        <input type="radio" name="categoria" value="Higiene Pessoal e Beleza"> Higiene Pessoal e Beleza <br>
        <input type="radio" name="categoria" value="Limpeza"> Limpeza <br>
        <input type="radio" name="categoria" value="Laticínios e Frios"> Laticínios e Frios <br>
        <input type="radio" name="categoria" value="Carnes"> Carnes <br> 
        <input type="radio" name="categoria" value="Hortifrúti"> Hortifrúti <br>
        <label>Preço R$</label> <br>
        <input type="number" name="precoProduto" step="any" required> <br>
        <label>Qntd. em Estqoue:</label> <br>
        <input type="number" name="qntdEstoque" required> <br>
        <input type="submit" value="Cadastrar produto">
    </form>

</body>
</html>