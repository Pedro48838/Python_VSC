'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será 
interrompido quando o número solicitado for negativo. '''

print("==" * 18)
print("TABUADA SUPREMA")
print("==" * 18)
print("Iremos calcular somente valores positivos!!")

while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("_" * 15)
    for c in range(1,11):
        print(f"{n} x {c} = {n * c}")
    print("_" * 15)
print("PROGRAMA ENCERRADO.")


























