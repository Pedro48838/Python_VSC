n1= float(input("Digite a primeira nota: "))
n2= float(input("Digite a segunda nota: "))
m= (n1 + n2)/2
#print("Média Boa!" if m >= 6.0 else "Sendo Burro!")
print(f"A sua média foi de {m:.1f}")
if m >= 6.0:
    print("Sua média foi boa!")
else:
    print("Você está sendo burro!")

"""1-Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu ou perdeu.
2-Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00, por cada km acima do limite.
3-Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
4-Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200 km e R$0.45 para viagens mais longas.
5-Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
6-Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
7-Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superirores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
8-Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
""" 

#==========================================================================================1

import random
import time #para manipular o tempo

pc= random.randint(0,5)
num= int(input("Pense e digite um número entre 0 e 5: "))
print("PROCESSANDO")
time.sleep(3) #manipular o tempo que eu quero que o programa avance 
if num == pc:
    print("Parabens, vc pensou igual o computador!!")
else:
    print(f"Vc não é pareo contra mim!! Eu pensei no {pc} e não no {num}")

#==========================================================================================2

import time 

vel= float(input("Digite a velocidade do seu carro: "))
print("COMPUTANDO")
time.sleep(1)
if vel > 80:
    print("Vocé foi multado. Limite excedido")
    multa= (vel - 80) * 7
    print(f"Sua multa será de R${multa:.2f}")
print("Bom dia, dirija com cuidado!")

#==========================================================================================3

num= int(input("Digite um número qualquer: "))
resul= num % 2 
if resul == 0:
    print("O numero é PAR!")
else:
    print("O numero é IMPAR!")

#==========================================================================================4

dist= float(input("Qual é a distancia da sua viagem? "))

print(f"Você está prestes a embarcar em uma viagem de {dist}Km.")
if dist <= 200:
    valor= dist * 0.50
else:
    valor= dist * 0.45
print(f"E o preço da sua passagem será de R${valor:.2f}")

#==========================================================================================5

from datetime import date
#para utilizar a condição do 0
ano= int(input("Que ano quer analizar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4== 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")

#==========================================================================================6

a= int(input("Digite o primeiro número: "))
b= int(input("Digite o segundo número: "))
c= int(input("Digite o terceiro número: "))

menor= a
#Verificando quem é o menor
if b<a and b<c:
    menor= b
if c<a and c<b:
    menor= c
#Verificando quem é o maior 
maior= a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior= c
print(f"O menor valor digitado foi {menor}.")
print(f"O maior valor digitado foi {maior}.")

#==========================================================================================7

sal= float(input("Digite o valor do seu sálario: R$ "))

print("Você está sendo um bom funcionario, por isso, ira receber um aumento, vamos calcular!")
if sal <= 1250.00:
    novo= sal + (sal * 15/100)
else:
    novo= sal + (sal * 10/100)
print(f"Quem ganhava R${sal}, passa a ganhar: R${novo} agora.")


#==========================================================================================8

r1= float(input("Primeiro segmento: "))
r2= float(input("Segundo segmento: "))
r3= float(input("Terceiro segmento: "))
if r1< r2 + r3 and r2< r1 + r3 and r3< r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triangulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triangulo!")







