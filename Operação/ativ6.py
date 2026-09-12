#Atividade 6:
#Calcule a porcentagem e dê um novo salário para o funcionário.

nome=input("Digite seu nome: ")
salario=float(input("Digite o seu salário atual:"))
porcentagem=float(input("Digite a porcentagem de aumento que você gostaria acrescentar ao salário: "))
novoSalário=salario+(salario*porcentagem)/100
print("Seu nome é:",nome,"e seu novo salário é: ", novoSalário)
