class Calculadora():
    def Somar(self, a, b):
        print("Resultado:", a+b)
    def Multiplicar(self, a, b):
        print("Resultado:", a*b)

calc1 = Calculadora() 

escolha = int(input("Escolha um método:\n1 - Somar\n2 - Multiplicar:\n"))

if escolha == 1:
    n1 = float(input("Digite um valor:\n"))
    n2 = float(input("Digite outro valor:\n"))
    calc1.Somar(n1, n2)

elif escolha == 2:
    n1 = float(input("Digite um valor:\n"))
    n2 = float(input("Digite outro valor:\n"))
    calc1.Multiplicar(n1, n2)