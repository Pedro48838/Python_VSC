''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

'''total = 0
totmil = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$ "))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == 'N':
        break
print(f"O total da compra foi R${total:.2f}.")
print(f"Temos {totmil} produtos custando mais de R$1000.00 reais.")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}.")'''

total = produtos_mais_1000 = produtos_comprados = preço_produto_mais_barato = 0
from time import sleep

print('-'*50)
print('        LOJA')
print('-'*50)
while True:
    nome_produto = str(input('Nome do produto: ')).strip().lower()
    preço_produto = float(input('Preço do produto: ').strip())
    produtos_comprados += 1

    total += preço_produto
    if preço_produto > 1000:
        produtos_mais_1000 += 1
    if produtos_comprados == 1:
        nome_produto_mais_barato = nome_produto
        preço_produto_mais_barato = preço_produto
    else:
        if preço_produto_mais_barato > preço_produto:
            preço_produto_mais_barato = preço_produto
            nome_produto_mais_barato = nome_produto

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('\033[;31mOpção Inválida! Tente de novo.\033[m')
        else:
            break
    if continuar == 'N':
        print(f'\033[;33mFinalizando as compras...\033[m')
        break
print('-'*50)
print(f'Total: {total}')
print(f'Produtos mais de R$1000: {produtos_mais_1000}')
print(f'Produto mais barato: {nome_produto_mais_barato} custando {preço_produto_mais_barato}')
print('-'*50)




































