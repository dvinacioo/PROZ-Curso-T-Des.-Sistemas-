# Dicionário para armexenar os alunos e idades

alunos = {}

# Lista de nomes predefinidos
nomes = ['Ana', 'Carlos', 'Bianca', 'Felipe']

# Pergunta a idade de cada açuno e salva no dicionário
for x in nomes:
    idade = input(f"Digite a idade de {x}: ") # entrada de idade
    alunos[x] = idade # Adicona ao dicionário

# Exibe a lista de alunos com sua idades
print("\n Lista de Alunos:")
for x, idade in alunos.items():
    print(f"{x}: {idade} anos")