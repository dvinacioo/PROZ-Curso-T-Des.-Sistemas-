<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Conserto de Eletrodomésticos</h1>
<div class="form">
    
        <form action="dados.php?agenda=consertoeletrodomesticos" method="post">
            <label>Nome:</label> <br>
            <input type="text" name="nomeCliente" required> <br>
    
            <label>Telefone para contato:</label> <br>
            <input type="tel" name="telefone" required> <br>
    
            <label>Aparelho com defeito:</label> <br>
            <select name="aparelhoSelecionado" required>
                <option value=""></option>
                <option value="Geladeira">Geladeira</option>
                <option value="Fogão">Fogão</option>
                <option value="Micro-ondas">Micro-ondas</option>
                <option value="Maquina de lavar roupas">Maquina de lavar roupas</option>
                <option value="Tanquinho">Tanquinho</option>
                <option value="Aspirador de Pó">Aspirador de Pó</option>
                <option value="Outro">Outro</option>
            </select> <br>
            <label>Outro:</label> <br>
            <input type="text" name="outroAparelho"> <br>
    
            <label>Data de atendimento:</label> <br>
            <input type="date" name="dataAtendimento" required> <br>
    
            <label>Descrição do problema:</label> <br>
            <textarea id="descri" rowns="4" cols="30" name="descricaoProblema" required> </textarea> <br>
    
            <input id="botao" type="submit" value="Requisitar Agendamento">
        </form>
    
</div>
</body>
</html>