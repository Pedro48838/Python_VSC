'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para 
viagens de até 200Km e R$0,45 parta viagens mais longas.'''

dist= float(input("Qual é a distancia da sua viagem? "))

print(f"Sua viagem terá {dist}Km.")
if dist <= 200:
    preço= dist * 0.50
else:
    preço= dist * 0.45
print(f"O preço da sua passagem será de R${preço:.2f}")



