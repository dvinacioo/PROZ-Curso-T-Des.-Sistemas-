"""
desenvolver um programa que automatize o cálculo de bônus para os funcionários. O bônus é calculado com base no desempenho individual, avaliado por uma pontuação que varia de 0 a 100. O programa deve solicitar a pontuação do funcionário e, com base nisso, determinar o valor do bônus a ser concedido.
Inicialmente, ele solicita ao usuário que insira a pontuação do funcionário. Dependendo dessa pontuação, o programa deve seguir um fluxo condicional. Se a pontuação for maior ou igual a 70, o funcionário recebe um bônus de 20% sobre o salário base. Se a pontuação for entre 50 e 69, o bônus é de 10%. Para pontuações abaixo de 50, não há bônus. O programa deve exibir o valor do bônus e uma mensagem personalizada sobre o desempenho.
- solicitar o saláario do funcionário
- solicitar a pontuação do funcionário
- se pontuação for Maior ou Igual a 70
    funcionário recebe + 20% de seu salário
- se pontuação for entre 50 e 69
    funcionário recebe + 10% de seu salário
- se pontuação for menor que 50
    funcionário não recebe bonus
"""
salario = float(input("Digite seu salário: "))
pontos = int(input("Entre 0 a 100, qual foi sua pontação no mês? "))
if pontos >= 70:
    total = (salario * 0.20) + salario

elif pontos > 49 and pontos < 70:
    total = (salario * 0.10)  + salario

else:
    total = salario + 0

print(f"Você receberá o valor de R$: {total:.2f}")