'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual 
foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random 
import time 

pc= random.randint(0, 5)

print("--==--" * 15)
print("Vamos brincar!!")
print("Irei pensar em um número entre 0 e 5, tente adivinhar... ")
print("--==--" * 15)

jogador = int(input("Em que número eu pensei ? "))
print("Precessando...")
time.sleep(2)
if jogador == pc:
    print("Parabens! Você me venceu...")
else:
    print(f"Ganhei!! Eu pensei no número {pc} e não no {jogador}...")
