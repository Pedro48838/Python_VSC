'''6-Faça um programa que leie o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
    Ex: Ana Maria de Souza
    primeiro: Ana
    ultimo: Souza'''

print("Iremos ler o seu nome e separa-lo!")

nome= str(input("Seu nome: ")).strip()
n= nome.split()

print(f"Seu primeiro nome é: {n[0]}")
print(f"Seu ultimo nome é: {n[len(n)-1]}")