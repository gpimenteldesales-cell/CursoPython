#Menu estruturado:

nome=(input("\nPor favor, digite como gostaria de ser chamado: "))

opcao = int(input(f"\n\nOlá {nome}, escolha uma opção abaixo:\n\n 1.Cadastrar seu produto no carrinho.\n 2.Buscar produtos.\n 3.Sair\n\n\n"))

match opcao:
    
    case 1:
        produtosCarrinho=["GTA VI", "RTX5050", "TECLADO MECÂNICO"]
        print("Opção 'Cadastrar seu produto no carrinho' selecionada.")
        nomeProduto=input("\nDigite o nome do produto que deseja comprar: ")
        preçoProduto=float(input("\nQual o valor do produto que deseja comprar? "))
        quantidadeProduto=int(input("\nQual a quantidade do produto que deseja comprar? "))
        compraDoProduto=preçoProduto*quantidadeProduto
        print(f"PRODUTO:{nomeProduto}\nQUANTIDADE:{quantidadeProduto}\n\nVALOR TOTAL:{compraDoProduto}")
        comprou=int(input("\n\nDigite '1' para colocar no carrinho\nDigite '2' para sair"))
        match comprou:
            case 1:
                produtoComprado=[nomeProduto, quantidadeProduto, compraDoProduto]
                produtosCarrinho.append(nomeProduto)
                print(f"\nTá quase!!\n\nCarrinho:\n\n{produtosCarrinho}\n\n")
            case 2:
                print("\nCompra cancelada.")
        
        
    case 2:
        produtosCarrinho=["GTA VI", "RTX5050", "TECLADO MECÂNICO"]
        print("\nOpção 'Buscar produtos do carrinho' selecionada.")
        print(f"\nCarrinho: {produtosCarrinho}")
        
        
    case 3:
        print("\n\nVolte logo!!!")
        
        
        
    case _:
        print("\n\nOpção inválida! Tente um número.")
        
        
        