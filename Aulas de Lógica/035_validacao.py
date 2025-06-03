import re


regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email = input("Digite um e-mail para validação: ")

if re.match(regex, email):
    print("\u2705 e-mail válido.")
    
else:
    print("\u274C email não é válido")