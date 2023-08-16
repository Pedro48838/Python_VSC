'''1-Crie um programa que leia um nome completo de uma pessoa e mostre:
    O nome com todas as letras maisculas
    O nome com todas as letras minusculas
    Quantas letras ao todo (sem considerar espaços)
    Quantas letras tem o primeiro nome'''

print("Para começar, digite seu nome completo, por favor!")

nome= str(input("Seu nome: "))

print(f"Com todas as letras maisculas, seu nome ficaria desse modo: {nome.upper()}")
print(f"E com todas as letras minusculas, ficaria: {nome.lower()}")
print(f"Ao todo seu nome tem {len(nome) - nome.count(' ')} letras") 
print(f"E seu primeiro nome tem {nome.find(' ')} letras.")