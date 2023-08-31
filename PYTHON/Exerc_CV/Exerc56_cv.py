'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print(f"-_-_-_-_ {p}ª -_-_-_-_")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()  #poderia colocar o .upper() 
    somaidade += idade
    if p == 1 and sexo in 'Mm':   #ao inves de ser =, foi colocado o in para que não importe se for maisculo ou minusculo
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'Mn' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
            if sexo in 'Ff' and idade < 20:
                totmulher20 += 1
mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos.")




















