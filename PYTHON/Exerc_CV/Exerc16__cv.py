'''1-Crie um programa que leia um num. real qq pelo teclado, e mostre na tela a sua porção inteira.
Ex: dig um num: 6.127.  O num 6.127 tem a parte inteira 6'''

import math

print("Vamos discorrer sobre a parte inteira de um número!")

num= float(input("Digite um número real: "))
print(f"O valor digitado {num}, e sua porção inteira é {math.trunc(num)}")
