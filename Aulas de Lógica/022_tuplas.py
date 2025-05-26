# Criando uma tupla com alguns elementos
frutas = ('Maçã', 'Banana', 'Cereja')

# Exibindo a tuplas
print("Minha tupla de frutas: ",frutas)

# Acessando elementos da tupla pelo índice

print("Minha primeira fruta: ",frutas[0])
print("Minha segunda fruta: ",frutas[1])
print("Minha terceira fruta: ",frutas[2])

# Descobrindo o tamanho da tupla
print("Números de frutas: ", len(frutas))

# Percorrendo a tupla com um loop
print("Listando todas as frutas na tupla:")
for x in frutas:
    print(x)

# Verificando se um elemento está na tupla
if 'Banana' in frutas:
    print("Banana está na tupla!")

# Criando um tupla de um único elemento.
unica_fruta = ('Melancia',) # (Nota se que em tuplas de um único elemento, devemos colocar "," no final dela.)
print("Tupla de um ínico elemento", unica_fruta)