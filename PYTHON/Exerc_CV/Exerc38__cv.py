''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

#Uma das maneiras de realizar o exercicio
print("Comparador!!!")

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
if n1 > n2:
    print(f"O {n1} é maior que o {n2}")           
elif n2 > n1:
    print(f"O {n2} é maior que o {n1}")
else:
    print("Não existe valor maior, os dois são iguais!")


#Segunda maneira de realizar

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n2 > n1:
    print("O SEGUNDO valor é maior")
elif n1 == n2:
    print("Os dois valores são IGUAIS")

#Terceira maneira, mais simplificada

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n2 > n1:
    print("O SEGUNDO valor é maior")
else:
    print("Os dois valores são iguais")
