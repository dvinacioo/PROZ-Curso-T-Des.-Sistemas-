# Verificação de número Divisível por 3 e por 5

num = int(input("Digite um valor qualquer: "))

if (num % 3 == 0):
    print("Este número é divisível por 3.")

elif (num % 5 == 0):
    print("Este número é divisível por 5.")

else:
    print("Este número não tem divisão exata por 3 ou 5.")