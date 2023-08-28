''' Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep 

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print("""Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA
""")

jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
print("-=-" * 10)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[computador]}")
print("-=-" * 10)
if computador == 0:      #COMPUTADOR jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA!!")
if computador == 1:       #COMPUTADOR jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA!!")
if computador == 2:       #COMPUTADOR jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:print("JOGADA INVALIDA!!")




















































