''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

print("__--__" * 15)
print("Conversos de bases decimais")
print("__--__" * 15)

num = int(input("Digite um numero inteiro qualquer: "))

print("""Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")

opção = int(input("Sua opção: "))
# [2:] esta relacionado a fatiamento, assim não aparecerá as nomenclaturas: 0x, 0o, 0b
if opção == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}") #0b para o python significa que é binário
elif opção == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}") #0o para o python significa que é octal
elif opção == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}") #0x para o python significa que é hexadecimal 
else:
    print("Opção invalida")

