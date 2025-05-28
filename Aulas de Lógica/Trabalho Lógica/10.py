# solicite um numero e determine se ele
# é positivo, negativo ou zero.

numero = float(input("Digite um núemro qualquer: "))

if numero == 0:
    print("O valor do seu número é 0")

elif numero > 0:
    print(f"O número {numero} é POSITIVO.")

else:
    print(f"O número {numero} é NEGATIVO")