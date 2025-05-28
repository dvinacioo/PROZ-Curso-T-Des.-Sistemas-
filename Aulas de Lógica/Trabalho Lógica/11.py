'''Peça ao usuário os comprimento dos três lados de um triangulo
e determine se é equilátero, isóceles ou escaleno'''

lado1 = float(input("Digite a mediada do primeiro lado: "))
lado2 = float(input("Digite a medida do segundo lado: "))
base = float(input("Digite a medida da base: "))

if lado1 == lado2 and lado2 == base:
    print("Seu trinagulo é um triangulo Equilátero.")


elif lado1 == lado2 and lado1 != base:
    print("O seu trinagulo é um triangulo Isósceles")

else:
    print("O seu triangulo é um triangulo Escaleno")   