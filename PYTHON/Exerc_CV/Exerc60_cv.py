'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 '''

'''from math import factorial

n = int(input("Digite um  número para calcular ser fatorial: "))
f = factorial(n)

print(f"O fatorial de {n} é {f}.")'''


n = int(input("Digite um número para calcular seu fatorial: "))
c= n
f = 1

print(f"Calculando {n}!")
while c > 0:
    print(f"{c}", end='')
    print(" x " if c > 1 else " = ", end='')
    f *= c  # f = f * c
    c -= 1
print(f"{f}")































