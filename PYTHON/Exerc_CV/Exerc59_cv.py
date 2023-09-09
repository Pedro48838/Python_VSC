''' : Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

print("Vamos trabalhar com dois valores inteiros !!")

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0  
while opcao != 5:
    print("""    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")
    opcao = int(input(">>>>>>> Qual é a sua opção? "))  
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} + {n2} é {soma}")
    elif opcao == 2:
        multi = n1 * n2
        print(f"A multiplicação entre {n1} x {n2} é {multi}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"Entre {n1} e {n2} o maior valor é {maior}")
    elif opcao == 4:
        print("Informe os novos números: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando... ")
        sleep(1)
    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 10)
print("Fim do programa! Volte sempre!")































