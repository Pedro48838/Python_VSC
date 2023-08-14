'''2-Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
    Ex: 1834
    unidade:4
    dezena:3
    centena:8
    milhar:1'''

print("Digite um número de 0 a 9999, que iremos analisa-lo")

num= int(input("Digite o número escolhido: "))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10

print(f"Analisando o número {num}, temos: ")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")