#Crie uma soma simples
print("Iremos realizar uma soma um pouco mais complexa!")

num1= int(input("Digite um valor: "))
num2= int(input("Digite outro valor: "))
num3= int(input("Digite outro valor: "))
num4= int(input("Por fim, digite outro valor: "))
soma1= num1 + num2
soma2= num3 + num4
total= soma1 + soma2

print("Para começar iremos verificar o valor da soma dos dois primeiros valores!")
print("A soma de {} + {} é igual a {}".format(num1, num2, soma1))
print("Agora iremos verificar o valor da soma dos dois ultimos valores!")
print("A soma de {} + {} é igual a {}".format(num3, num4, soma2))
print("Como nós temos o resultado das somas, vamos ver com o resultado da soma total")
print("O resultado do primeiro conjuto, {} + o resultado do segundo conjunto {}, é igual a {}".format(soma1, soma2, total))
print("Parabens !! Você conseguiu realizar uma soma simples, seu(a) primata")