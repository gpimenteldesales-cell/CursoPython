#Atividade 5:
#Faça um programa em Python que solicite o nome de um funcionário e o seu salário atual.
#Em seguida, solicite o valor do aumento salarial. O programa deverá calcular e exibir o nome do
#funcionário e seu novo salário.

nome=input("Digite seu nome: ")
salarioAtual=int(input("Digite seu valor salário atual: "))
print("Olá,",nome,"seu salário atual é", salarioAtual,"Quanto gostaria de receber futuramente?")
salarioFuturo=int(input("Digite um salário que gostaria de receber futuramente: "))
print("Perfeito",nome,"seu pedido de aumento para: ",salarioFuturo,"está em análise. Retornaremos seu resultado enviando-o um email.")