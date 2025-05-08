#CALCULADORA BÁSICA EM PYTHON
num1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = float(input("DIGITE O SEGUNDO NÚMERO: "))

if num2 != 0:
    divisao = num1 / num2

else:
    divisao = "**ERRO** DIVISÃO POR 0 NÃO É PERMITIDO."

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"A SOMA dos valores é: {soma}")
print(f"A SUBTRAÇÃO dos valores é: {subtracao}")
print(f"A DIVISÃO dos valores é: {divisao}")
print(f"A MULTIPLICAÇÃO dos valores é: {multiplicacao}")