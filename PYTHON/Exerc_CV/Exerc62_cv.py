''' Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser
que quer mostrar 0 termos.'''

print("GERADOR DE PA")
print("-=-" * 10)

prim = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais #  total = total + mais 
    while cont <= total:
        print(f"{termo} -> ", end='')
        termo += razao 
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")


















