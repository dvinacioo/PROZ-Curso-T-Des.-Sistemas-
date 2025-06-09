def validar_formato(data):
    """Valida o formato da data DD/MM/AAAA"""
    partes = data.split('/')
    if len(partes) != 3:
        return False  # Não tem 3 partes (DD, MM, AAA)
    
    dia, mes, ano = partes
    
    # Verificar se dia, mês e ano têm o número correto de dígitos
    if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
        return False
    
    # Verificar se são números
    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        return False

    return True

def validar_mes(mes):
    """Valida se o mês é entre 01 e 12"""
    if int(mes) < 1 or int(mes) > 12:
        return False
    else:
        return True

def dias_no_mes(mes, ano):
    """Retorna o número de dias no mês, levando em consideração anos bissextos"""
    dias_por_mes = {
        '01': 31, '02': 28, '03': 31, '04': 30,
        '05': 31, '06': 30, '07': 31, '08': 31,
        '09': 30, '10': 31, '11': 30, '12': 31
    }

    # Verificar se é fevereiro e o ano é bissexto
    if mes == '02' and ano_bissexto(ano):
        return 29
    return dias_por_mes[mes]
    
def validar_dia(dia, mes, ano):
    """Valida se o dia é válido para o mês"""
    if int(dia) < 1 or int(dia) > dias_no_mes(mes, ano):
        return False
    return True

def ano_bissexto(ano):
    """Retorna True se o ano for bissexto"""
    ano = int(ano)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

def validar_data(data):
    """Valida uma data no formato DD/MM/AAAA"""
    if not validar_formato(data):
        return False  # Formato inválido
    
    partes = data.split('/')
    dia, mes, ano = partes
    
    # Validar mês
    if not validar_mes(mes):
        return False
    
    # Validar dia
    if not validar_dia(dia, mes, ano):
        return False
    
    return True

data = input("Digite uma data no formato DD/MM/AAAA: ") 

if validar_data(data):
    print(f"A data {data} é válida!")
else:
    print(f"A data {data} é inválida!")
