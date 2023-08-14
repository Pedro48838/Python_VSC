'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print("-_-_-" * 15)
print("Banco dos pobres")
print("-_-_-" * 15)

casa= float(input("Qual o valor da casa: R$ "))
sal = float(input("Qual o seu salario: R$ "))
anos= int(input("Quantos anos de financiamento? "))
prestação= casa / (anos * 12)
minimo= sal * 30 / 100

print(f"Para pagar uma casa de R$ {casa :.2f}, em {anos}.") #O end é para que continue na mesma linha
print(f"A Prestação será de R$ {prestação :.2f}")
if prestação <= minimo:
    print("Emprestimo pode ser CONCEDIDO!")
else:
    print("Emprestimo NEGADO!")

#Faça sempre por partes !!!!!!








