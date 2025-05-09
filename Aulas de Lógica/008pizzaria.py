# MENU DE UMA PIZZARIA

print("PIZZARIA BOM SABOR - SEJA BEM VINDO")
print("______CARDÁPIO - PREÇOS______")
print(" ")
print("******** PIZZAS - SABORES ********")
print(" CALABREZA, FRANGO, CATUPIRY ")
print("******** PIZZAS - TAMANHO ********")
print(" PIZZA PEQUENA  R$ 12,00  ")
print(" PIZZA MÉDIA  R$ 17,00  ")
print(" PIZZA GRANDE  R$ 23,00  ")
print("******** REFRIGERANTES ********")
print("  COCA-COLA     R$ 7,00")
print("  GUARANA       R$ 6,00")
print("  FANTA         R$ 5,00")
print("_"*16)
print(" ")

print("FAÇA O SEU PEDIDO PARA PIZZA")
print("1 - CALABREZA")
print("2 - FRANGO")
print("3 - CATUPIRY")
print("_"*16)
pedidopizza = int(input())

print("DIGITE O TAMANHO DA PIZZA:")
print(" P - PEQUENA")
print(" M - MÉDIA")
print(" G - GRANDE")
print("_"*16)
tampizza = input().upper()

print("FAÇA SEU PEDIDO PARA REFRIGERANTE: ")
print(" 1 - COCA COLA")
print(" 2 - GUARANÁ")
print(" 3 - FANTA")
pedidorefri = int(input())

if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1):
    preco = 12.00 + 7.00
    pedidos = "CALABREZA, PEQUENA, COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    preco = 17.00 + 7.00
    pedidos = "CALABREZA, MÉDIA, COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    preco = 23.00 + 7.00
    pedidos = "CALABREZA, GRANDE, COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1):
    preco = 12.00 + 7.00
    pedidos = "FRANGO, PEQUENA, COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    preco = 17.00 + 7.00
    pedidos = "FRANGO, MÉDIA, COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    preco = 23.00 + 7.00
    pedidos = "FRANGO, GRANDE, COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    preco = 12.00 + 7.00
    pedidos = "CATUPIRY, PEQUENA, COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
    preco = 17.00 + 7.00
    pedidos = "CATUPIRY, MÉDIA, COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    preco = 23.00 + 7.00
    pedidos= "CATUPIRY, GRANDE, COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    preco = 12.00 + 6.00
    pedidos = "CALABREZA, PEQUENA, GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    preco =  17.00 + 6.00
    pedidos = "CALABREZA, MÉDIA, GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    preco = 23.00 + 6.00
    pedidos = "CALABREZA, GRANDE, GUARANÁ"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    preco = 12.00 + 6.00
    pedidos = "FRANGO, PEQUENO, GUARANÁ"

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2):
    preco = 17.00 + 6.00
    pedidos = "FRANGO, MÉDIA, GUARANÁ"

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2):
    preco = 23.00 + 6.00
    pedidos = "FRANGO, GRANDE, GUARANÁ"

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
    preco = 17.00 + 6.00
    pedidos = "CATUPIRY, MÉDIA, GUARANÁ"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2):
    preco = 23.00 + 6.00
    pedidos = "CATUPIRY, GRANDE, GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    preco = 12.00 + 5.00
    pedidos = "CALABREZA, PEQUENA, FANTA"

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 3):
    preco = 17.00 + 5.00
    pedidos = "CALABREZA, MÉDIA, FANTA"

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    preco = 23.00 + 5.00
    pedidos = "CALABREZA, GRANDE, FANTA"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3):
    preco = 12.00 + 5.00
    pedidos = "FRANGO, PEQUENA, FANTA"

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
    preco = 17.00 + 5.00
    pedidos = "FRANGO, MÉDIA, FANTA"

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
    preco = 23.00 + 5.00
    pedidos = "FRANGO, GRANDE, FANTA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3):
    preco = 12.00 + 5.00
    pedidos = "CATUPIRY, PEQUENA, FANTA"

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    preco = 17.00 + 5.00
    pedidos = "CATUPIRY, MÉDIA, FANTA"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    preco = 23.00 + 5.00
    pedidos = "CATUPIRY, GRANDE, FANTA"

print("_"*16)
print(f"O TOTAL A PAGAR É: R$ {preco:.2f}")
print(f"OS PEDIDOS FORAM: {pedidos}")
print("_"*16)
print("BOM APETITE E VOLTE SEMPRE!")