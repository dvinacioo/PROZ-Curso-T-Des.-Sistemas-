MATRIZ = [[0] * 4 for _ in range(4)]
# Preenche a linha de índice 0 da matriz:
# Atribui o valor 0 ao elemento na linha 0, coluna 0
MATRIZ[0][0] = 0
MATRIZ[0][1] = 1
MATRIZ[0][2] = 0
MATRIZ[0][3] = 1

MATRIZ[1][0] = 0
MATRIZ[1][1] = 0
MATRIZ[1][2] = 1
MATRIZ[1][3] = 0


for contador1 in range(4):
    # Loop interno para percorrer os índices das colunas
    for contador2 in range(4):
        print(MATRIZ[contador1][contador2], end=" ")
    print()