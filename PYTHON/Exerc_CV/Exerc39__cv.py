'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao 
serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o 
tempo que falta ou que passou do prazo.'''

print("|--|--|" * 20)
print("ALISTAMENTO MILITAR")
print("|--|--|" * 20)

from datetime import date
atual = date.today().year
ano = int(input("Digite o ano de seu nascimento: "))
idade = atual - ano

print(f"Quem nasceu em {ano} tem {idade} anos em {atual}.")
if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE.")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o alistamento.")
    ano = atual + saldo
    print(f"Seu alistamento será em {ano}.")
elif idade > 18:
    saldo = idade - 18 
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    ano = atual - saldo 
    print(f"Seu alistamento foi em {ano}.")





















