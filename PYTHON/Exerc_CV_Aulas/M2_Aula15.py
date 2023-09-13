'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print("Acabou")'''

'''cont = 1
while True:   ##irá gerar um loop infinito
    print(cont, '-> ', end='')
    cont += 1
print("Acabou")'''

'''n = cont = 0
while cont < 5:   #irá ler 5 números
    n = int(input("Digite um número: "))
    cont += 1'''

'''n = s = 0
while n != 999:  ##Irá continuar prosseguindo até atingit a flag
    n = int(input("Digite um número: "))
    s += 1
s -= 999  #isó e uma gambiarra 
print(f"A soma vale {s}")'''

n = s = 0
while True: 
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")

























