# Calculadora de Juros Simples
""" Solicite ai usuário um valor principal, a taxa de juros (em porcentagem) e o número de anos. Calcule o montante
final utilizando a fórmula: MOntante = principal + (principal*taxa de juros* anos / 100)."""

valor_principal = float(input("Digite o valor principal de sua aplciação: R$"))
juros = float(input("Quantos de juros de você receberá? "))
anos = int(input("Quantos anos vai ter sua aplicação? "))
total = valor_principal + (valor_principal * juros * anos / 100)
print(f"Vai retornar R${total:.2f} após o investimento.")