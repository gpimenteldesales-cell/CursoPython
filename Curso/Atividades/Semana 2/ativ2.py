#Faça um programa em Python que solicite o nome de um produto, seu preço e a quantidade comprada.
#O programa deverá calcular e exibir: o nome do produto e o valor total da compra.

nomeProduto=input("Digite o nome do produto que deseja comprar: ")
preçoProduto=float(input("Qual o valor do produto que deseja comprar? "))
quantidadeProduto=int(input("Qual a quantidade do produto que deseja comprar? "))
compraDoProduto=preçoProduto*quantidadeProduto
print("PRODUTO: ",nomeProduto)
print("QUANTIDADE: ",quantidadeProduto)
print("VALOR TOTAL:",compraDoProduto)