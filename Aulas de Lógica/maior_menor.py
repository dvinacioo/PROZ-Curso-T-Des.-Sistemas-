#ESTE PROGRAMA COMPRA 3 NÚMEROS E INFORMA QUAL É O MAIOR, O MENOR E TAMBÉM A MÉDIA ENTRE ELES

num1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
num3 = float(input("DIGITE O TERCEIRO NÚMERO: "))

if (num1 > num2) and (num1 > num3):
    maior = num1
    
elif (num2 > num1) and (num2 > num3):
    maior = num2
    
else:
    maior = num3

if (num1 < num2) and (num1 < num3):
    menor = num1
    
elif (num2 < num1) and (num2 < num3):
    menor = num2
    
else:
    menor = num3
media = (num1 + num2 + num3) / 3
print(f"O maior número é {maior}")
print(f"O menor dos números é {menor}")
print(f"A média entre os 3 números é {media:.2f}")