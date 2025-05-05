"""Faça um programa que calcule o valor de desconto para um determinado produto,
faça um Print Screen do código fonte do seu programa e do programa em execução.
● OBS: No programa deve aparecer o seu nome, deve permitir que o usuário digite o
código do produto, o valor do produto, o valor da porcentagem do desconto. No final deve ser
calculado e apresentado o valor total a pagar.
"""
aluno = input("DIGITE SEU NOME:")
produto = input("NOME DO PRODUTO: ")
valor = float(input("DIGITE O VALOR DO PRODUTO: R$ "))
desconto = float(input("DIGITE A % DO DESCONTO: "))
valor_desconto = valor * (desconto / 100)
valor_final = valor - valor_desconto
print(f"O valor a ser pago é: R$ {valor_final:.2f}")