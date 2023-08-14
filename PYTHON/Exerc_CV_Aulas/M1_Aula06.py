# Crie um programa que leia dois numeros, e mostre a soma entre elas.
num1= int(input("Digite um número: "))
num2= int(input("Digite outro número: "))
soma= num1 + num2

print("Você acabou de somar dois números inteiros!")
print("A soma de {} + {} é igual a {}.".format(num1, num2, soma))

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as inf. possíveis sobre ele
coisa= input("Digite qualquer coisa: ")
print(type(coisa))
print(coisa.isalnum())
print(coisa.isalpha())
print(coisa.isascii())
print(coisa.isdecimal())
print(coisa.isidentifier())
print(coisa.islower())
print(coisa.isupper())