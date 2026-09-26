# ATIVIDADE – CÁLCULO DE DESCONTO POR FAIXA SALARIAL 
# Desenvolva um programa em Python que solicite ao usuário o seu salário bruto. Com 
# base no salário informado, o programa deverá identificar a faixa salarial e aplicar a alíquota 
# correspondente.

salarioBruto=float(input("Digite seu salário bruto: "))
desconto=float(0)

def Calculo_Desconto():
    descontoTotal = (salarioBruto/100) * desconto
    salarioLiquido = salarioBruto - descontoTotal
    print(f"Seu salário atual é : R${salarioLiquido}\nDesconto: R${descontoTotal}")
    
if salarioBruto <= 1621:
    desconto = 7,5
    Calculo_Desconto()
elif salarioBruto <= 2902.84:
    desconto = 9
    Calculo_Desconto()
elif salarioBruto <= 4354.27:
    desconto = 12
    Calculo_Desconto()
elif salarioBruto <= 8475.55:
    desconto = 14
    Calculo_Desconto()
else:
    print("Você é RICO!!!")
    