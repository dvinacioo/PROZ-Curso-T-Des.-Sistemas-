# Calculadora de Desconto
""" Peça ao usuário o valor de um produto e o percentual de descinto. Calcule e mostre o calor com desconto aplicado.
"""

valor_produto = float(input("Digite o valor do produto: R$"))
desconto = int(input("Digite a % de desconto: "))
desconto_aplicado = valor_produto  * ( desconto / 100)
total = valor_produto - desconto_aplicado
print(f"O valor Total do Produto vai se de R${total:.2f}")