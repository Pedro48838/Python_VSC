''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''


peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"Seu IMC é de {imc:.1f}")
if imc < 18.5:
    print("Você está abaixo do peso normal.")
# elif imc >= 18.5 and imc < 25: PODE SER DESSA FORMA
elif 18.5 <= imc < 25:
    print("PARABENS, você está na faixa de peso normal")
elif 25 <= imc < 30:
    print("Você está em sobrepeso")
elif 30 <= imc < 40:
    print("Você está em obesidade, cuidado!")
elif imc >= 40:
    print("Você está em obesidade morbida, cuidado!")























