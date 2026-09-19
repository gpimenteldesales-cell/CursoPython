nome=(input("Digite seu nome: "))
idade=int(input("Digite a sua idade: "))

print(f"Olá, {nome},essas são suas informações:")

# idade
if idade >= 60:
    print("Idoso")

elif idade >= 18:
    print("Adulto")

elif idade >= 12:
    print("Adolescente")

else:
    print("Criança")
    