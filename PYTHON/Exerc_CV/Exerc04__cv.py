# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print("Iremos neste exercicio, dissecar uma palavra!")

coisa= input("Digite alguma coisa! ")

print("O tipo primitivo desse valor é : ", type(coisa))
print("É alfanumerico ? ", coisa.isalnum())
print("É alfabético ? ", coisa.isalpha())
print("Está na tabela ascii ? ", coisa.isascii())
print("Está em decimal ? ", coisa.isdecimal())
print("Está em digitos ? ", coisa.isdigit())
print("Está em minusculas ? ", coisa.islower())
print("É um número ? ", coisa.isnumeric())
print("Pode utilizar o print ? ", coisa.isprintable())
print("Só tem espaços ? ", coisa.isspace())
print("Está capitalizada ? ", coisa.istitle())
print("Está em maísculas ? ", coisa.isupper())
