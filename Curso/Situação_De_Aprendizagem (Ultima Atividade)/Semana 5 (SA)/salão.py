from datetime import date


class Servico:
    def __init__(self):
        self.nome = ""
        self.valor = 0.0
        self.dia = 0
        self.mes = 0
        self.ano = 0
        self.hora = 0
        self.minuto = 0

    def colocar_nome(self, nome):
        self.nome = nome

    def colocar_valor(self, valor):
        self.valor = valor

    def colocar_data(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def colocar_horario(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def mostrar_servico(self):
        print("--------------------")
        print("Serviço: " + self.nome)
        print("Valor: R$ " + "%.2f" % self.valor)
        print("Data: " + str(self.dia).zfill(2) + "/" + str(self.mes).zfill(2) + "/" + str(self.ano))
        print("Horário: " + str(self.hora).zfill(2) + ":" + str(self.minuto).zfill(2))
        print("--------------------")


class Agendamento:
    def __init__(self):
        self.cliente = ""
        self.servico = ""

    def colocar_cliente(self, cliente):
        self.cliente = cliente

    def colocar_servico(self, servico):
        self.servico = servico

    def mostrar_agendamento(self):
        print("====================")
        print("AGENDAMENTO CONFIRMADO")
        print("Cliente: " + self.cliente)
        print("Serviço: " + self.servico.nome)
        print("Valor: R$ " + "%.2f" % self.servico.valor)
        print("Data: " + str(self.servico.dia).zfill(2) + "/" + str(self.servico.mes).zfill(2) + "/" + str(self.servico.ano))
        print("Horário: " + str(self.servico.hora).zfill(2) + ":" + str(self.servico.minuto).zfill(2))
        print("====================")


def pular_linha():
    print("")


def mostrar_menu():
    pular_linha()
    print("===== SALÃO DE BELEZA =====")
    print("1 - Cadastrar serviço")
    print("2 - Listar serviço")
    print("3 - Realizar agendamento")
    print("4 - Ver agendamento")
    print("5 - Sair")
    pular_linha()


def pedir_texto(mensagem):
    texto = ""
    while texto.strip() == "":
        texto = input(mensagem)
        if texto.strip() == "":
            print("Não pode ficar vazio! Digite de novo.")
    return texto.strip()


def pedir_valor():
    valor = 0.0
    valor_certo = False
    while valor_certo == False:
        texto = input("Digite o valor do serviço: ")
        texto = texto.replace(",", ".")
        try:
            valor = float(texto)
            if valor > 0:
                valor_certo = True
            else:
                print("O valor precisa ser maior que zero!")
        except ValueError:
            print("Valor inválido! Digite só números, por exemplo 50 ou 49.90")
    return valor


def pedir_data():
    dia = 0
    mes = 0
    ano = 0
    data_certa = False
    while data_certa == False:
        texto = input("Digite a data (dd/mm/aaaa): ")
        partes = texto.split("/")
        if len(partes) != 3:
            print("Data inválida! Use o formato dd/mm/aaaa.")
        elif partes[0].isdecimal() == False or partes[1].isdecimal() == False or partes[2].isdecimal() == False:
            print("Data inválida! Digite só números e barras.")
        else:
            dia = int(partes[0])
            mes = int(partes[1])
            ano = int(partes[2])
            if ano < 1000 or ano > 9999:
                print("Ano inválido!")
            elif mes < 1 or mes > 12:
                print("Mês inválido!")
            else:
                dias_do_mes = 31
                if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    dias_do_mes = 30
                elif mes == 2:
                    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
                        dias_do_mes = 29
                    else:
                        dias_do_mes = 28
                if dia < 1 or dia > dias_do_mes:
                    print("Esse dia não existe nesse mês!")
                elif date(ano, mes, dia) < date.today():
                    print("Essa data já passou! Digite uma data de hoje em diante.")
                else:
                    data_certa = True
    return dia, mes, ano


def pedir_horario():
    hora = 0
    minuto = 0
    horario_certo = False
    while horario_certo == False:
        texto = input("Digite o horário (hh:mm): ")
        partes = texto.split(":")
        if len(partes) != 2:
            print("Horário inválido! Use o formato hh:mm.")
        elif partes[0].isdecimal() == False or partes[1].isdecimal() == False:
            print("Horário inválido! Digite só números e dois pontos.")
        else:
            hora = int(partes[0])
            minuto = int(partes[1])
            if hora < 0 or hora > 23:
                print("Hora inválida! Tem que ser de 0 a 23.")
            elif minuto < 0 or minuto > 59:
                print("Minuto inválido! Tem que ser de 0 a 59.")
            else:
                horario_certo = True
    return hora, minuto


def principal():
    servico_cadastrado = False
    agendamento_feito = False
    servico = Servico()
    agendamento = Agendamento()
    continuar = "sim"

    while continuar == "sim":
        mostrar_menu()
        opcao = input("Digite a opção: ")

        if opcao == "1":
            servico = Servico()
            nome = pedir_texto("Digite o nome do serviço: ")
            servico.colocar_nome(nome)
            valor = pedir_valor()
            servico.colocar_valor(valor)
            dia, mes, ano = pedir_data()
            servico.colocar_data(dia, mes, ano)
            hora, minuto = pedir_horario()
            servico.colocar_horario(hora, minuto)
            servico_cadastrado = True
            agendamento_feito = False
            print("Serviço cadastrado com sucesos!")

        elif opcao == "2":
            if servico_cadastrado == True:
                servico.mostrar_servico()
            elif servico_cadastrado == False:
                print("Nenhum serviço cadastrado ainda.")

        elif opcao == "3":
            if servico_cadastrado == False:
                print("Você presisa cadastrar um serviço primeiro!")
            elif servico_cadastrado == True:
                agendamento = Agendamento()
                cliente = pedir_texto("Digite o nome do cliente: ")
                agendamento.colocar_cliente(cliente)
                agendamento.colocar_servico(servico)
                agendamento_feito = True
                print("Agendamento realizado com sucesso!")

        elif opcao == "4":
            if agendamento_feito == False:
                print("Nenhum agendamento foi realizado ainda.")
            elif agendamento_feito == True:
                agendamento.mostrar_agendamento()

        elif opcao == "5":
            print("Enserrando o programa... Até logo!")
            continuar = "nao"

        else:
            print("Opção inválida!")


principal()