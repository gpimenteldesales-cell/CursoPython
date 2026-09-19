#Menu estruturado:
opcao = int(input(f"\n\n\nEscolha uma opção:\n1.Cadastrar seu produto no carrinho.\n2.Buscar produtos.\n3.Sair\n\n\n"))

match opcao:
    
    case 1:
        print("Opção 'Cadastrar seu produto no carrinho' selecionada.")
        
    case 2:
        print("Opção 'Buscar produtos' selecionada.")
    case 3:
        print("Volte logo!!!")
    case _:
        print("Opção inválida! Tente um número.")