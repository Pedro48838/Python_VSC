'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 
500.'''

for c in range(1,501, 2):
    if c % 3 == 0:   
        print(c, end= ' ') #Somente mostrando sem a soma 


soma = 0
cont = 0

for c in range(1,501, 2):
    if c % 3 == 0:
        cont = cont + 1 # cont += 1
        soma = soma + c # soma += c
print(f"A soma de todos os {cont} valores solicitados é {soma}.")















