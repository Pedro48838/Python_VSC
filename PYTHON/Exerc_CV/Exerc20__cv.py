import random
'''O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que 
leia o nome dos 4 alunos e mostre a ordem sorteada. '''

print("Iremos agora, utilizar a mesma sala, só que sortear todos os alunos em uma ordem aleatória")

print("Digite os nomes dos 6 alunos:")

al1= input("Aluno 01: ")
al2= input("Aluno 02: ")
al3= input("Aluno 03: ")
al4= input("Aluno 04: ")
al5= input("Aluno 05: ")
al6= input("Aluno 06: ")

lista = [al1, al2, al3, al4, al5, al6]

random.shuffle(lista)

print(f"A ordem sorteada foi: {lista}")