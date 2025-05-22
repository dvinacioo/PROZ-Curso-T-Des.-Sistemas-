vetor = [0, 0, 0, 0]

for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor[i] = (numero)
print(vetor)

negativos = 0

for i in range(4):
    if vetor[i] < 0:
        print(f"o {vetor[i]} que está na posição {i+1} é negativo.")
        negativos += 1
        
if negativos == 0:
    print("Não há valores negativos")
else:
    print(f"Como pode ver, o seu vetor possui {negativos} valores negativos.")
       