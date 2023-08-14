def obter_informacoes_casa():
    print("Bem-vindo ao programa de cálculo de circuitos elétricos e energia solar!")
    print("Por favor, forneça as seguintes informações sobre a residência/comércio:")

    while True:
        tipo_estabelecimento = input("Tipo de estabelecimento (residencial ou comercial): ").strip().lower()
        if "residencial" in tipo_estabelecimento:
            tipo_estabelecimento = "residencial"
            break
        elif "comercial" in tipo_estabelecimento:
            tipo_estabelecimento = "comercial"
            break
        else:
            print("Tipo de estabelecimento inválido. Por favor, informe 'residencial' ou 'comercial'.")

    area = obter_numero("Área do local (em metros quadrados): ")
    num_comodos = obter_numero_inteiro("Número de cômodos com tomada: ")
    regiao = input("Região onde está localizado o local da casa/estabelecimento: ")

    print("Obrigado por fornecer as informações!")
    return tipo_estabelecimento, area, num_comodos, regiao


def obter_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, informe um número decimal.")


def obter_numero_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, informe um número inteiro.")


# Chamada da função para obter as informações
tipo_estabelecimento, area, num_comodos, regiao = obter_informacoes_casa()

# Exibição das informações obtidas
print("Tipo de estabelecimento:", tipo_estabelecimento)
print("Área:", area)
print("Número de cômodos com tomada:", num_comodos)
print("Região:", regiao)
