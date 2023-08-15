'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média 
atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

#Primeira maneira de realizar o exercicio

print("||--||" * 12)
print("Escola de Tangamandapio")
print("||--||" * 12)

print("Aluno, digite as notas disponiveis.")

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

if media > 7.0:
    print(f"Sua média é de: {media}. Parabens, vc está APROVADO.")
elif media < 5:
    print(f"Sua média é de: {media}. Infelizmente você está REPORVADO.")
elif media >= 5 and media < 7:
    print(f"Sua média é de: {media}. Você esta de RECUPERAÇÃO.")


#Segunda maneira de reaizar o exercicio

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2

print(f"Tirando {nota1 :.1f} e {nota2 :.1f}, a média do aluno é {media :.1f}")
if 7 > media >= 5:
    print("O aluno está em RECUPERAÇÃO")
elif media < 5:
    print("O aluno está REPROVADO")
elif media >= 7:
    print("O aluno está APROVADO")
 









































