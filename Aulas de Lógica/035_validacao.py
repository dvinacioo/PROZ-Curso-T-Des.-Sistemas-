import re


regex = r'^[w\.-]+@[w\.-]+\.w+$'

email = input("Digite um e-mail para validação: ")

if re.match(regex, email):
    print("\u2705 e-mail válido.")
    
else:
    print("\u274C email não é válido")