import calculadora

n1 = float(input("Digite o primeiro valor:\n"))
n2 = float(input("Digite o segundo valor:\n"))

def EscolhaUsuarioDef():

    escolha = float (input("Escolha uma opção:\n1 - Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar\n"))

    if escolha == 1:
        print("Sua conta resultou em:\n", calculadora.somar(n1,n2))

    elif escolha == 2:
        print("Sua conta resultou em:\n", calculadora.subtrair(n1,n2))

    elif escolha == 3:
        print("Sua conta resultou em:\n", calculadora.dividir(n1,n2))

    elif escolha == 4:
        print("Sua conta resultou em:\n", calculadora.multiplicar(n1,n2))

    else:
        print ("Digite um valor válido.")
        EscolhaUsuarioDef()
    return

EscolhaUsuarioDef()