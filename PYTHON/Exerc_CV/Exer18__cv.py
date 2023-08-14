'''Faça um programa que leia um angulo qq e mostre na tela o valor do seno, cosseno e tangente desse angulo.'''

print("Iremos voltar para os tempos de escola!")
print("Escolha um angulo que iremos calcular seu seno, cosseno e sua tangente")

import math

ang= float(input("Digite o angulo escolhido: "))
sen= math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tang= math.tan(math.radians(ang))

print(f"O angulo escolhido tem o valor de seno: {sen:.2f}")
print(f"E seu cosseno: {cos:.2f}")
print(f"E por fim, sua tangente: {tang:.2f}")

