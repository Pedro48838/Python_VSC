import random
'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
e escrevendo o nome escolhido.'''

print("Iremos sortear um aluno entre 6 que serão escolhidos!")

print("Digite os nomes dos 6 alunos:")

al1= input("Aluno 01: ")
al2= input("Aluno 02: ")
al3= input("Aluno 03: ")
al4= input("Aluno 04: ")
al5= input("Aluno 05: ")
al6= input("Aluno 06: ")

lista= [al1, al2, al3, al4, al5, al6]

escolhido= random.choice(lista)

print(f"O aluno escolhido é: {escolhido}")
