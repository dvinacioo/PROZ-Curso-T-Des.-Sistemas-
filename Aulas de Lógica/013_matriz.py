MATRIZ = [[0] * 4 for _ in range(4)]
# Preenche a linha de índice 0 da matriz:
# Atribui o valor 0 ao elemento na linha 0, coluna 0
MATRIZ[0][0] = 0
MATRIZ[0][1] = 1
MATRIZ[0][2] = 0
MATRIZ[0][3] = 1

print("Linha 0:")
for contador1 in range(4):  
    print(MATRIZ[0][contador1])

print("\nLinha 1:")

for contador1 in range(4):
    print(MATRIZ[1][contador1])

