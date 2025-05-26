# Dicionário é uma estrutura de dados que armazena pares de chave-valor.
# As chaves devem ser únicas e imutáveis (como strings, números ou tuplas), e cada chave aponta para um valor.
# Dicionários são úteis para representar dados estruturados, como informações de uma pessoa ou configurações.
# Eles são definidos com chaves {}.

# Exemplo de dicionário:
usuario = {
    'nome': 'Daniela',
    'sobrenome': 'Souza',
    'profissão': 'Analista de Sistemas',
    'filhos': 'Melina'
}

print(usuario['nome'])
print(usuario['sobrenome'])
print(usuario['profissão'])
print(usuario['filhos'])
print() #Quebra de linha na saída

# Para verificar a wuantidae de elementos do dicionário
print(len(usuario))