# Laço com Contador e Acumulador
totalCopos = 0

while totalCopos < 8:
    coposBebidos = int(input("Digite a quantidade de copos de água que você bebeu:\n"))
    totalCopos = totalCopos + coposBebidos
    print(f"Você bebeu: {totalCopos} copos!")
print("Parabéns! Meta de hidratação atingida!")

# Contagem Regressiva
tempo = int(input("Digite o tempo(segundos) inicial da contagem:\n"))

while tempo > 0:
    print(f"Tempo restante: {tempo}")
    tempo = tempo - 1
print ("Tempo esgotado! Decolar!")