""" Soicite a idade do usuário e classifque-0 em:
"Criança", "Adolescente", "Adulto-Jovem" ou "Adulto"
"""
idade = int(input("Digite a sua idade: "))
etaria = ""
if idade <= 13:
    etaria = "Criança"
    print(f"Você é classificado como: {etaria}")

elif idade >= 14 and idade < 18:
    etaria = "Adolescentente"
    print(f"Você é classifcado como: {etaria}")

elif idade >= 18 and idade < 26:
    etaria = "Adulto-Jovem"
    print(f"Você é classifcado como: {etaria}")

elif idade >= 27:
    etaria = "Adulto"
    print(f"Você é classifcado como: {etaria}")