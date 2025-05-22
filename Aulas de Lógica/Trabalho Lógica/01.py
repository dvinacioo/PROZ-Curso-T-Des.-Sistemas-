""""
Crie um programa que pergunte ao usuário  o valor do café (um número) e pergunte para ele quantos cafés ele irá querer comprar 
e apresente o resultado a pagar
"""

valor = float(input("Qual o valor do café? R$ "))
quantidade = int(input("Quantos cafés você irá comprar? "))

total = valor * quantidade

print(f"Você pagara R$ {total:.2f} por {quantidade} cafés")