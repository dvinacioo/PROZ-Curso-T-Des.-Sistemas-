# Troca de Valores
""" Solicite ao usuário dois valores e troque o valor da primeira variável com o da segunda variável,
e vice - versa"""


valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")


valor1, valor2 = valor2, valor1


print(f"Agora, o primeiro valor é: {valor1}")
print(f"E o segundo valor é: {valor2}")
