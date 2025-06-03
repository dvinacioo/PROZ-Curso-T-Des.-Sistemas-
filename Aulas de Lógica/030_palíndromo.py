palavra = input("Digtite uma palavra: ") # Pega a digitação dp usuário
inverter = palavra[::-1] # Inverte a string digitada pelo usuário

print(f"Texto digitado: {palavra}")
print(f"Texto invertido: {inverter}")
if inverter == palavra:
    print("Sua palavra é um palíndromo.")

else:
    print("Sua palavra não é um palíndromo.")