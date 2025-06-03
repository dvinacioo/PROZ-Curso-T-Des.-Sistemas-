def validar_nome(nome):
    # Verifica se todos os caracteres do nome são Letras
    if nome.isalpha():
        return True
    
    else:
        return False
    
def validar_idade(idade):
    # Verifica se todos os  caracteres da idade dígitos
    if idade.isdigit():
        return True
    
    else:
        return False
    
# Solicita que o usuário digite os dados
nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")


# Valida o nome do usuário usando a função validar_nome(nome)
if validar_nome(nome):
    print("Nome válido.")
    
else:
    print("Nome inválido! O nome deve conter apenas letras.")
    
# Valida a idade do usuário usando a função validar_idade(idade)
if validar_idade(idade):
    print("Idade válida.")
    
else:
    print("Idade inválida! A idade deve conter apenas númeoros.")