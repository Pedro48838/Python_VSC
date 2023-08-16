'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print("__--__==__--" * 12)
print("Vamos analisar triangulos!!")
print("__--__==__--" * 12)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos PODEM FORMAR um triangulo!")
else:
    print("Os segmentos NÃO PODEM FORMAR um tringulo!")







