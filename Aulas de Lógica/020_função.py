# Cria a função que calcula os dias 
def calc(idade):
    return (idade * 365)
    
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
resultado = calc(idade)

print(f"Olá {nome}! Você viveu já aproximadamente {resultado} dias")