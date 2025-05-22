# Cálculo de IMC
"""Peça ao usuário seu peso (em kg) e alutra (em metros), e calcule o Índice de Massa Corporal (IMC)
utilizando a fórmula> IMCM = peso / (altura * altura)"""
peso = float(input("Digite seu em em (kg): "))
altura = float(input("Digite sua altura: "))
IMC =  peso / (altura * altura) 
print(f"Seu índice IMC é de {IMC:.2f}")