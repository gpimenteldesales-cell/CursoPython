# ATIVIDADE – ORGANIZANDO A LISTA DE COMPRAS 
# Você precisa organizar uma lista de compras do supermercado. Durante a preparação da 
# lista, percebeu que precisa adicionar, inserir e remover produtos. 
# Crie inicialmente a seguinte lista: 
# compras = ["arroz", "feijão", "macarrão", "açúcar"] 
# O programa deverá realizar as seguintes operações: 
# 1. Solicitar ao usuário um produto que foi esquecido e adicioná-lo no final da lista. 
# 2. Solicitar outro produto e a posição onde ele deverá ser colocado na lista. 
# 3. Solicitar o nome de um produto que não será mais comprado e removê-lo. 
# 4. Ao final, apresentar a lista de compras atualizada.

compras = ["arroz", "feijão", "macarrão", "açúcar"]

print(f"A sua lista de compras é \n{compras}\nEscolha um dos numeros com base na sua preferência\n")
escolha=int(input("1.Esqueceu um produto\n2.Quer adicionar produto em prioridade\n3.Deseja Remover um produto da lista\n"))

if escolha == 1:
    produtoEsquecido=(input("Você esqueceu algo? Digite o que esqueceu!! "))
    compras.append(produtoEsquecido)
    print(compras)

elif escolha == 2:
    ordemProduto=(input("Adicione um produto com prioridade: "))
    compras.insert(0, ordemProduto)
    print(compras)

elif escolha == 3:
    removeProduto=(input("Escolha um produto para remover da lista: "))
    compras.remove(removeProduto)
    print(compras)

else:
    print("Tchau!")