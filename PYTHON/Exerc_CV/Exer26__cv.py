'''5-Faça um programa que leia uma frase pelo teclado e mostre:
    Quantas vezes aparece a letra A
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece a ultima vez '''

print("A seguir digite uma frase qualquer.")

frase= str(input("Frase: ")).strip()

print(f"Vamos descobrir quantas vezes a letra A aparece. A letra 'A' apareceu {frase.count('A')} vezes.")
print(f"A letra 'A', apareceu pela primeira vez na {frase.find('A')+1} posição")
print(f"E apareceu a ultima vez na {frase.rfind('A')} posição")