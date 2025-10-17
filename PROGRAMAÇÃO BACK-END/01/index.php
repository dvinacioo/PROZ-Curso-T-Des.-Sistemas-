<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    

<?php
$num1 = 10;
$num2 = 20;
$soma = $num1 + $num2;
$sub = $num1 - $num2;
$mult = $num1 * $num2;
$div = $num1 / $num2;
echo "A soma de $num1 + $num2 é: $soma";
echo "<br>";
echo "A subtração de $num1 - $num2 é: $sub";
echo "<br>";
echo "A multiplicação de $num1 * $num2 é: $mult";
echo "<br>";
echo "A divisão de $num1 / $num2 é: $div";
echo "<br>";

if($div > 2){
    echo "A divisão é maior que 2";
}
elseif($div < 2){
    echo "A divisão é menor que 2";
}
else{
    echo "A divisão é igual a 2";
}
?>
</body>
</html>