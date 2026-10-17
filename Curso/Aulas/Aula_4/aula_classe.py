class Produto:
    porcentagem = 0.10

    def Imposto(self, valor):
        print ("Imposto: ", valor * self.porcentagem)
    def Desconto(self, valor):
        print("Desconto: ", valor * self.porcentagem)

produto1 = Produto()

produto1.Imposto(float(input("Digite um valor:\n")))
produto1.Desconto(float(input("Digite um valor:\n")))