import med

nomeAluno = input("Digite seu nome:\n")
print(f"\nOlá {nomeAluno}, descubra sua média do ano!\n")

n1 = float (input("Digite sua primeira nota do trimestre:\n"))
n2 = float (input("Digite sua segunda nota do trimestre:\n"))
n3 = float (input("Digite sua terceira nota do trimestre:\n"))
mediaFinal = med.media(n1,n2,n3)
print(f"\nAluno: {nomeAluno}\nMédia:{mediaFinal}")

if mediaFinal >= 6:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")