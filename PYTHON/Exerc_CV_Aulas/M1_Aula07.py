'''1-Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
2-Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
3-Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
4-Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
5-Faça um programa que leia um número inteiro qq e mostre na sua tela a sua tabuada.
6-Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. [$1,00= 3,27R$]
7-Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta nec. para 
pinta-la, sabendo que a cada litro de tinta, pinta uma aréa de 2m².
8-Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. Com 5% de desconto.
9-Faça um algoritmo que leia o salário de um funcionario e mostre o seu novo salario, com 15% de aumento.'''

#1-

num1= int(input("Digite um numero inteiro "))
print("O número sucessor ao seu escolhido é {}!".format(num1 + 1))
print("O antecessor é {}!".format(num1 - 1))

#2- 

print("Pense um número!")

num1= int(input("Digite o seu número escolhido: "))
print("O dobro do escolhido é : {}".format(num1 * 2))
print("O triplo do escolhido é : {}".format(num1 * 3 ))

print("Agora vamos calcular a sua raiz quadrada")
print("A raiz quadrada do escolhido é : {:.5f}".format(num1 **(1/2)))

#3-

print("Boletin Escolar do aluno Roludison Belo Anus do Rego")

nota1= float(input("Digite sua primeira nota: "))
nota2= float(input("Digite sua segunda nota: "))

print("A sua média é {}.".format((nota1 + nota2) / 2))

#4-

print("Conversor de medidas")
print("Digite um valor, que o mesmo será apresentado em metros! ")

num= float(input(""))

print("O valor escolhido em cm é: {} cm".format(num * 100))
print("O valor escolhido em milimetros é: {} mm".format(num * 1000))

#5- 

print("TABUADA DOS VIRGENS SEM ESPERANÇA")

num= int(input("Digite um numero inteiro: "))

print(" {} x 1 = {}".format(num, num * 1))
print(" {} x 2 = {}".format(num, num * 2))
print(f" {num} x 3 = {num * 3}")
print(f" {num} x 4 = {num * 4}")
print(f" {num} x 5 = {num * 5}")
print(f" {num} x 6 = {num * 6}")
print(f" {num} x 7 = {num * 7}")
print(f" {num} x 8 = {num * 8}")
print(f" {num} x 9 = {num * 9}")
print(f" {num} x 10 = {num * 10}")
'''for i in range(0, 11):
    print(f"{num} x {i} = {num * i}")'''

#6- 

print("Quanto dinheiro vc tem na carteira ? ")

din= float(input("Digite a quantia: "))
print(f"Em dolares vc teria: {din / 3.27:.2f}")

#7-

#8-

print("Digite o valor de um produto: ")

prod= float(input(""))
desc= prod * 0.05

print("O valor do produto está com 5% de desconto!")
print("Então o valor saíra por: {:.2f} reais".format(prod - desc))

#9-

sal= float(input("Qual o seu salário: "))
aum= sal * 0.15
print("Com um aumento de 15%, você, seu assalariado fudido, será de: {:.2f}".format(sal + aum))