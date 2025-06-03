opcao = -1

while True:
    
    print("-"*40)
    print("1 - Dizer olá")
    print("2 - Dizer oi")
    print("0 - Sair do programa")
    print("-"*40)
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
    except ValueError:
        print("Entrada inválida. Digite um número.")
        
    else:
        
        if opcao == 1:
            print("Olá.")
            
        elif opcao == 2:
            print("Oi.")
            
        elif opcao == 0:
            print("Saindo do programa...")
            
        else:
            print("Opção inválida. Tente novamente.")
            
    if opcao == 0:
        break