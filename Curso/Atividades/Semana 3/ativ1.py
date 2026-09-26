# Checar Maioridade
idade = int(input("Digite sua idade: \n"))

if idade >= 18:
    print("Acesso Autorizado")
else:
    print("Acesso não autorizado")

# Verificar Número Positivo
num = int (input("Digite um número inteiro: \n"))

if num >= 0:
    print("Número é positivo")
else:
    print("Número é negativo")
    
# Autenticação de Senha
pin = 1234
inp = int(input("Digite a o PIN\n"))

if inp == pin:
    print("Login realizado com sucesso.")
else:
    print("Saia!!")

# Pesquisa em Lista
frutas = ["maçã", "banana", "laranja"]
escolhaFrutas = input(f"{frutas}\nEscolha um produto do estoque:\n").lower()


if escolhaFrutas in frutas:
    print("Fruta disponivel no estoque.")
else:
    print("Fruta indisponivel no estoque.")
    
# Confirmação de Ação
sim = input("Digite 'sim' para receber uma notificação\n")

if sim == "sim":
    print ("Enviando notificação...\n")
else:
    print ("Não notificado.\n")