#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele 
#foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km= float(input("Quantos quilometros foram percorridos: "))
dias= float(input("Por quantos dias você permaneceu com o carro: "))
kmr= km * 0.15
kmd= dias * 60

print(f"Sabendo que você rodou por {km}km e por {dias:.0f} dias.\nVamos calcular o seu gasto!")
print(f"O valor por km rodado é: {kmr}R$ e por dias em que permaneceu com o carro: {kmd}R$.")
print(f"Seu gasto total é de: {kmr + kmd}R$")





