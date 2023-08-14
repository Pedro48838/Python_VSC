'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

import time

vel= float(input("Qual a  velocidade atual do carro ? "))
time.sleep(1)
if vel > 80:
    print("MULTADO! Limite de 80 Km/h excedido")
    multa= (vel - 80) * 7
    print(f"Você deve pagar uma multa de R${multa:.2f}\n")

print("Tenha um bom dia e dirija com cuidado!")