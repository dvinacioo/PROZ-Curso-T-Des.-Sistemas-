# Lista para armazenar os nomes cadastrados
cadastro = []

while True:
    print("\n1 - Adicionar nome\n2 - Listar nomes\n3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ") # Usuário digita o nome
        cadastro.append(nome) # Nome pe adicionado à lista


    elif opcao == "2":
        print("\n Lista dos nomes: ")
        for nome in cadastro: # Exibe todos os cadastros
            print(nome) 

    
    elif opcao == "3":
        print("Saindo do programa...")
        break # Finaliza o programa

    
    else:
        print("Opção inválida! Tente novamente")