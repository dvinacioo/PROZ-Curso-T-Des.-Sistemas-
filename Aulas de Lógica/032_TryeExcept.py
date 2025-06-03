# Exivindo as opções do usuário
print(""" 1 - JANEIRO
2 - FEVEREIRO
3 - MARÇO
4 - ABRIL
5 - MAIO
6 - JUNHO
7 - JULHO
8 - AGOSTO
9 - SETEMBRO
10 - OUTUBRO
11 - NOVEMBRO
12 - DEZEMBRO """)

# le e valida a entrada
try:
    numero = int(input("Sua escolha: "))
    
    # Usa match-case para identificar o mes
    match numero:
        case 1:
            mes = "JANEIRO"
            
        case 2:
            mes = "FEVEREIRO"
            
        case 3:
            mes = "MARÇO"
            
        case 4:
            mes = "ABRIL"
            
        case 5:
            mes = "MAIO"    
        
        case 6:
            mes = "JUNHO"
            
        case 7:
            mes = "JULHO"
            
        case 8:
            mes = "AGOSTO"
            
        case 9:
            mes = "SETEMBRO"
            
        case 10:
            mes = "OUTUBRO"
            
        case 11: 
            mes = "NOVEMBRO"
            
        case 12: 
            mes = "DEZEMBRO"
            
except ValueError:
    mes = "ENTRADA INVÁLIDA. DIGITE NOVAMENTE"
    
print(f"Sua escolha foi {mes}")