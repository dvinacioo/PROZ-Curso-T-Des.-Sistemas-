"""Peça uma temperatura em Celsius ao usário e converta-a para Fahrenheit utilizando a fórmula:
F = (C * 9/5) + 32
"""
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A tempratura em Fahrenheit é {fahrenheit:.2f}")