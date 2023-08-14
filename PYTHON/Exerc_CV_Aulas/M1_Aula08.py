'''1-Crie um programa que leia um num. real qq pelo teclado, e mostre na tela a sua porção inteira.
Ex: dig um num: 6.127.  O num 6.127 tem a parte inteira 6
2- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre 
o comprimento da hipotenusa
3-Faça um programa que leia um angulo qq e mostre na tela o valor do seno, cosseno e tangente desse angulo.
4- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
e escrevendo o nome escolhido.
5- O mesmo professor do exercicio anteriorquer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que 
leia o nome dos 4 alunos e mostre a ordem sorteada. 
6- Faça um programa em python que abra e reproduza o audio de um arquivo MP3'''

#==========================================================================================1

import math
# from math import trunc (math.trunc ficaria somente trunc)
num = float(input("Digite um valor: "))
print(f"O valor digitado é {num}, e sua proção inteira é {math.trunc(num)}")
#SEM A BIBLIOTECA == ... é {int(num)}

#==========================================================================================2

import math
co= float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi= math.hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa vai medir: {hi:.2f}")

#==========================================================================================3

import math

ang= float(input("Digite o angulo que você deseja: "))

seno= math.sin(math.radians(ang))
print(f"O angulo de {ang}, tem o SENO de {seno:.2f}")
cos= math.cos(math.radians(ang))
print(f"O angulo de {ang}, tem o COSSENO de {cos:.2f}")
tang= math.tan(math.radians(ang))
print(f"O angulo de {ang}, tem a TANGENTE de {tang:.2f}")

#==========================================================================================4

import random

n1= input("primeiro aluno: ")
n2= input("segundo aluno: ")
n3= input("terceiro aluno: ")
n4= input("quarto aluno: ")

lista = [n1, n2, n3, n4]

escolhido= random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")

#==========================================================================================5

import random

n1= input("primeiro aluno: ")
n2= input("segundo aluno: ")
n3= input("terceiro aluno: ")
n4= input("quarto aluno: ")

lista= [n1, n2, n3, n4]

random.shuffle(lista)

print(f"A ordemd e apresentação será:\n {lista}")

#==========================================================================================6



