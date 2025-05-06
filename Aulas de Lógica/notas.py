# PROGRAMA PARA VERIFICAR SE O ALUNO PASSOU

nota = float(input("DIGITE SUA NOTA(O a 10): "))

while nota < 0 or  nota > 10:

    print("Erro! -A NOTA DEVE SER ENTRE 0 A 10!-")

    nota = float(input("DIGITE A NOTA NOVAMENTE(O a 10): "))

if nota >= 7:
    print("ALUNO APROVADO")

else:
    print("ALUNO REPROVADO")