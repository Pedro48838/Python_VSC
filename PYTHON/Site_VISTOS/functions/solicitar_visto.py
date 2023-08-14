def solicitar_visto(destino):
    opcoes_visto = {
        "Portugal": {
            1: "Preencher formulário de solicitação",
            2: "Agendar entrevista",
            3: "Enviar documentação"
        },
        "Estados Unidos": {
            1: "Preencher formulário de solicitação",
            2: "Pagar taxa de solicitação",
            3: "Agendar entrevista"
        }
    }
    
    if destino in opcoes_visto:
        print(f"Opções de solicitação de visto para {destino}:")
        for opcao, descricao in opcoes_visto[destino].items():
            print(f"{opcao} - {descricao}")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if int(opcao) in opcoes_visto[destino]:
            print(f"Executando opção {opcao} - {opcoes_visto[destino][int(opcao)]}")
            # Lógica específica para a opção selecionada
        else:
            print("Opção inválida. Por favor, digite um número válido.")
    else:
        print("Destino inválido.")

# Exemplo de lógica específica para Portugal
def solicitar_visto_portugal():
    print("Opções de solicitação de visto para Portugal:")
    print("1 - Preencher formulário de solicitação")
    print("2 - Agendar entrevista")
    print("3 - Enviar documentação")
    
    while True:
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao.isdigit() and int(opcao) in [1, 2, 3]:
            opcao = int(opcao)
            
            if opcao == 1:
                print("Preenchendo formulário de solicitação...")
                # Lógica para preencher formulário de solicitação para Portugal
                print("Formulário de solicitação preenchido com sucesso!")
                break
            elif opcao == 2:
                print("Agendando entrevista...")
                # Lógica para agendar entrevista para Portugal
                print("Entrevista agendada com sucesso!")
                break
            elif opcao == 3:
                print("Enviando documentação...")
                # Lógica para enviar documentação para Portugal
                print("Documentação enviada com sucesso!")
                break
        else:
            print("Opção inválida. Por favor, digite um número válido.")

# Exemplo de lógica específica para os Estados Unidos
def solicitar_visto_estados_unidos():
    print("Opções de solicitação de visto para os Estados Unidos:")
    print("1 - Preencher formulário de solicitação")
    print("2 - Pagar taxa de solicitação")
    print("3 - Agendar entrevista")
    
    while True:
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao.isdigit() and int(opcao) in [1, 2, 3]:
            opcao = int(opcao)
            
            if opcao == 1:
                print("Preenchendo formulário de solicitação...")
                # Lógica para preencher formulário de solicitação para os Estados Unidos
                print("Formulário de solicitação preenchido com sucesso!")
                break
            elif opcao == 2:
                print("Realizando pagamento da taxa de solicitação...")
                # Lógica para pagar taxa de solicitação para os Estados Unidos
                print("Taxa de solicitação paga com sucesso!")
                break
            elif opcao == 3:
                print("Agendando entrevista...")
                # Lógica para agendar entrevista para os Estados Unidos
                print("Entrevista agendada com sucesso!")
                break
        else:
            print("Opção inválida. Por favor, digite um número válido.")
