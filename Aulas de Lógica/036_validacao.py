import re

def validar_nome(nome):
    # Definindo a padronização da expressão regular para aceitar somente letras
    padrao = '^[a-zA-Z]+$'
    
    if re.match(padrao, nome):
        return True
    
    else:
        return False

def validadar_idade(idade):
    padrao = '^[0-9]+$'
    
    if re.match(padrao, idade):
        return True
    
    else:
        return False

nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

if validar_nome(nome) and validadar_idade(idade):
    print("Nome e idades válidos!")
    
else:
    print("Nome e idades inválidos!")