'''2- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre 
o comprimento da hipotenusa'''

print("Vamos calcular os catetos de um triangulo retangulo e calcular sua hipotenusa")

import math

co= float(input("Digite o cateto oposto: "))
ca= float(input("Digite o cateto adjacente: "))
hip= math.hypot(co, ca)

print(f"O triangulo escolhido, tem seu cateto oposto {co} , seu cateto adjacente {ca} \n e por fim, o calculo de sua hipotenusa tem o resultado de {hip:.2f}")
print("FIM!!")