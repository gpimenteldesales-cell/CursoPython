# Classificação por Faixa Etária
idade = int(input("Digite sua idade para descobrir sua faixa etária!!!\n"))

if idade < 12:
    print("Criança")

elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")

# Controle de Sinal de Trânsito
cor = ["verde", "amarelo", "vermelho"]
pergunta = input(f"{cor}\nEscreva a cor atual do semáforo\n").lower()

if pergunta in cor[0]:
    print("Siga em frente!")

elif pergunta in cor[1]:
    print("Atenção! Desacelere.")

else:
    print("Pare!")

# Calculadora de Desconto
valorCompra = float(input("Digite o valor total da sua compra:\nR$:"))
desconto = [20, 10]

if valorCompra >= 500:
    compra = valorCompra * (1 - desconto[0] / 100)
    print (f"Sua compra teve um desconto de 20%\nValor total R${compra}")
    
elif valorCompra >= 200:
    compra = valorCompra * (1 - desconto[1] / 100)
    print (f"Sua compra teve um desconto de 10%\nValor total: R${compra}")

else:
    print(f"Valor: R${valorCompra}")
    
# Diagnóstico de IMC
imc = float(input("Digite seu IMC\n(Digite um valor real)\n"))

if imc < 18.5:
    print("Abaixo do peso.")

elif imc < 25.0:
    print("Saudável.")

else:
    print("Acima do peso.")
    
# Validação de Turno

hora = int(input("Digite a hora atual:\n"))

if hora <= 11:
    print("Manhã")

elif hora <= 17:
    print("Tarde")

elif hora <=22:
    print("Noite")

else:
    print("Fora de turno")