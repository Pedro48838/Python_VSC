'''3-Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'''

nom= str(input("Por favor, digite o nome da sua cidade: ")).strip()

print(nom[:5].upper() == 'SANTO')

