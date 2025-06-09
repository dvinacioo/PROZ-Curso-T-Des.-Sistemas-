def limpar_cpf(cpf):
    # Limpa o CPF, removendo pontos e hífen
    return cpf.replace(".", "").replace("-", "").strip()

def validar_cpf(cpf):
    # Valida o CPF, verificando o formato e os dígitos verificadores
    cpf = limpar_cpf(cpf)

    # Etapa 1: Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Etapa 2: Verificar se todos os dígitos são iguais (CPF como '11111111111')
    if cpf == cpf[0] * 11:
        return False

    # Etapa 3: Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)  # Pesos: 10, 9, 8, ..., 2

    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Etapa 4: Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):  # Agora inclui o primeiro dígito
        soma += int(cpf[i]) * (11 - i)  # Pesos: 11, 10, 9, ..., 2

    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Etapa 5: Comparar os dígitos verificadores com os últimos números do CPF
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False

# Programa principal
cpf_input = input("Digite o CPF (formato: XXX.XXX.XXX-XX): ")

if validar_cpf(cpf_input):
    print("CPF válido!")
else:
    print("CPF inválido!")
