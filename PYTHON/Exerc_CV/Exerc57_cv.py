''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação 
novamente até ter um valor correto. '''

sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]  #O [0] é usado para mostrar somente a primeira letra 
while sexo not in 'MF':  #while not sexo == 'M' and sexo == 'F'
    sexo = str(input("Dados ínvalidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")






















































