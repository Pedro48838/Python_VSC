'''1-Crie um programa que leia um nome completo de uma pessoa e mostre:
    O nome com todas as letras maisculas
    O nome com todas as letras minusculas
    Quantas letras ao todo (sem considerar espaços)
    Quantas letras tem o primeiro nome
2-Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
    Ex: 1834
    unidade:4
    dezena:3
    centena:8
    milhar:1
3-Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'
4-Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
5-Faça um programa que leia uma frase pelo teclado e mostre:
    Quantas vezes aparece a letra A
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece a ultima vez 
6-Faça um programa que leie o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
    Ex: Ana Maria de Souza
    primeiro: Ana
    ultimo: Souza
'''
#1

nome= input("Digite o seu nome completo: ").strip()
#.strip() no inicio é para já retirar espaços que usuario pode colocar
print("Seu nome somente com letras maisculas ficaria: ")
print(f"{nome.upper()}")
print(f"Com todas as letras em minusculas:\n {nome.lower()}")
print(f"Seu nome ao todo tem {len(nome) - nome.count(' ')} letras.")
print(f"Seu primeiro nome tem {nome.find(' ')} letras.")
#para contar quantas letras tem o primeiro nome= nome.find(' ')

#2

num= int(input("Digite um número entre 0 e 9999: "))
#n= str(num) Poderia ser usado como string
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print(f"Analisando o número {num}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")

#3

cid= str(input("Digite o nome de uma cidade: ")).strip()
print(cid[:5].upper() == 'SANTO')

#4

nome= str(input("Digite o seu nome: ")).strip()
print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}") 

#5

frase= str(input("Digite uma frase: ")).strip().upper()
print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"A letra A apareceu na posição {frase.find('A')+1} ")
print(f"A ultima letra A apareceu na posição {frase.rfind('A')+1}")

#6

nome= str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome é : {nome}")
n= nome.split()
print(f"Seu primeiro nome é {n[0]}")
print(f"Seu ultimo nome é {n[len(n)-1]}")
