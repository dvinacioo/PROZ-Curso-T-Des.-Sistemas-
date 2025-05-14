# Inicalizamos listas com zeros para definir o tamanho,
NOME = [0] * 3
IDADE = [0] * 3
TELEFONE = [0] * 3
RUA = [0] * 3
NUMERO = [0] * 3
BAIRRO = [0] * 3
# A variável 'cont' é usada como índice para percorrer as listas
cont = 0

# Loop 'for' em Python que intera de 0 até 2 (inclusive).
for cont in range(3):
    # Imprime o cabeçalho do cadastro, incrementando 'cont' para exibir o cadastro
    print(f"---- {cont + 1}° - CADASTRO ----")
    print()

    # Solicita e lê o  as informações do Usuário;
    print("Digite o seu nome: ")
    NOME[cont] = input()


    print("Digite a sua idade: ")
    IDADE[cont] = int(input())

    print("Digite o seu Telefone:")
    TELEFONE[cont] = input()

    print("Digite seu Endereço:")
    RUA[cont] = input("Rua: ")
    NUMERO[cont] = input("Número: ")
    BAIRRO[cont] = input("Bairro: ")
    print("\n" * 20)

    # Outro loop 'for' para exibir os daddos cadastrados.
    # Imprime os dados de cada Usuário.
for cont in range(3):
    print(f"NOME: {NOME[cont]}")
    print(f"IDADE: {IDADE[cont]} anos")
    print(f"Número: {NUMERO}")
    print(f"Endereço: {RUA[cont]}, {NUMERO[cont]} - {BAIRRO[cont]}")
    print("-"*20)