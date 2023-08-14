def menu():
    while True:
        print("Bem-vindo(a) a Oba Vistos!")
        print("Selecione uma opção:")
        print("1 - Cadastrar novo usuário")
        print("2 - Solicitar visto para Portugal")
        print("3 - Solicitar visto para os Estados Unidos")
        print("4 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao.isdigit():
            opcao = int(opcao)

            if opcao == 1:
                # Lógica para cadastrar novo usuário
                break
            elif opcao == 2:
                # Lógica para solicitar visto para Portugal
                break
            elif opcao == 3:
                # Lógica para solicitar visto para os Estados Unidos
                break
            elif opcao == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Por favor, digite um número válido (1 a 4).")
        else:
            print("Opção inválida! Por favor, digite um número válido (1 a 4).")

menu()
