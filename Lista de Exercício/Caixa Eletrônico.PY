saldo = 1000

while True:
    print("\n1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Valor do depósito: R$ "))
        saldo += valor
        print("Depósito realizado!")

    elif opcao == "3":
        valor = float(input("Valor do saque: R$ "))

        if valor <= saldo:
            saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "4":
        break

    else:
        print("Opção inválida.")