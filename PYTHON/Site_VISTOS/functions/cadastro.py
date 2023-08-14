import re

def cadastrar_usuario(usuarios):
    while True:
        nome = input("Digite seu nome completo: ")
        email = input("Digite seu e-mail: ")
        
        telefone = input("Digite seu número de telefone (com código de área e DDD): ")
        while not re.match(r"\+\d{1,3}\s?\(\d{2}\)\s?\d{4,5}\-\d{4}", telefone):
            print("O número de telefone deve estar no formato correto. Por favor, tente novamente.")
            telefone = input("Digite seu número de telefone (com código de área e DDD): ")
        
        idade = input("Digite sua idade: ")
        while not idade.isdigit():
            print("A idade deve ser um número inteiro. Por favor, tente novamente.")
            idade = input("Digite sua idade: ")

        senha = input("Digite sua senha: ")
        confirmar_senha = input("Confirme sua senha: ")

        if senha == confirmar_senha:
            usuario_existente = False
            for usuario in usuarios:
                if usuario['email'] == email:
                    usuario_existente = True
                    break
            
            if usuario_existente:
                print("Já existe um usuário cadastrado com este e-mail. Por favor, tente novamente.")
            else:
                usuario = {
                    "nome": nome,
                    "email": email,
                    "telefone": telefone,
                    "idade": idade,
                    "senha": senha
                }
                usuarios.append(usuario)
                print("Usuário cadastrado com sucesso!")
                break
        else:
            print("As senhas não coincidem. Por favor, tente novamente.")

usuarios = []
cadastrar_usuario(usuarios)
