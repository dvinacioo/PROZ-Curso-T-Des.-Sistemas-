def verficaSexo(sexo):
    if sexo == "f":
        print("Feminino")

    elif sexo == "m":
        print("Masculino")
    else:
        print("Digitação inválida.")
        verficaSexo(sexo)

print("Digite o seu sexo (F para feminino) e (M para masculino)")

sexo = input()

verficaSexo(sexo)