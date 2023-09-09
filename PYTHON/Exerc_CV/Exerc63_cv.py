''' Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

print("-_-_-" * 10)
print("SEQUENCIA DE FIBONACCI")
print("-_-_-" * 10)

n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1

print("~" * 30)

print(f"{t1} -> {t2}", end='')

cont = 3   #irá começar em 3, pq já mostrei o 1º e 2º termo
while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3
    cont += 1
print(" -> FIM")
print("~" * 30)


























