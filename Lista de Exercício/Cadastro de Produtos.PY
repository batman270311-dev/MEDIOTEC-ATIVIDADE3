produtos = []

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        produto = input("Nome do produto: ")
        produtos.append(produto)
        print("Produto cadastrado!")

    elif opcao == "2":
        print("\nProdutos:")
        for produto in produtos:
            print("-", produto)

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")