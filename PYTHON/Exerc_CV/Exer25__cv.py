'''4-Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome'''

print("Iremos descobrir se você possui SILVA, no seu nome!")

nome= str(input("Digite seu nome:")).strip()

print(f"Seu nome tem SILVA? {'SILVA' in nome.upper()}")