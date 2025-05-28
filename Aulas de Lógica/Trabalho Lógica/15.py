""" Solicite ao usuário o valor de um profuto e
calcule o valor com desconto apensa se o valor original
foir mais que R$100,00"""

valor_produto = float(input("Digite o valor do produto que deseja comprar: "))

if valor_produto <= 100:
    print("Com este valor você não possui desconto.")
    print(f"Sua compra vai ficar no valor de {valor_produto:.2f}")

elif valor_produto > 100 and valor_produto <= 250:
    print("Com este valor, Você ganha 5% de desconto.")
    desconto = valor_produto * 0.05
    print(f"Sua compra vai ficar no valor de {valor_produto - desconto:.2f}")

elif valor_produto > 250 and valor_produto <= 500:
    print("Com esse valor, Você ganha 10% de desconto")
    desconto = valor_produto * 0.10
    print(f"Sua compra vai ficar no valor de {valor_produto - desconto:.2f}")

elif valor_produto > 500:
    print("Com esse valor, Você ganha 13% de desconto")
    desconto = valor_produto * 0.13
    print(f"Sua compra vai ficar no valor de {valor_produto - desconto:.2f}")