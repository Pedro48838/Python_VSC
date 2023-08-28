for c in range(0,6):
    print("Oi")
print("Fim") #Cuidado com a identação


for c in range(1,6): #Se quiser contar de 1 atpe 6, precisa colocar(1,7)
    print(c)
print("Fim")


for c in range(6,0, -1): #Para contagem regressiva, poderia colocar 2(pulando de 2 em dois)
    print(c)
print("Fim")


n = int(input("Digite um número: "))

for c in range(0, n+1): #o +1 é para que aparece o número desejado
    print(c)
print("Fim")


i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("Fim")


s = 0
for c in range(0,4):
    n = int(input("Digite um valor: "))
    s = s + n # Ou pode ser digitado no Python da seguinte maneira: s += n
print(f"O somatório de todos os valores foi {s}")























