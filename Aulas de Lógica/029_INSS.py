# Contribuição do INSS

salario = float(input("Digite o valor do seu salário: R$ "))

if salario <= 1692.72:
    recolhimento = salario * 0.08

elif salario > 1692.72 and salario <= 2822.90:
    recolhimento = salario * 0.09

elif salario > 2822.90 and salario <= 5645.90:
    recolhimento = salario * 0.11

total = salario - recolhimento

print(f"O valor recolhido de seu salário de vai ser de: R${recolhimento:.2f}")
print(f"E você receberá: R${total:.2f}")