#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de 
#tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print("Calculo de tinta")

lar= float(input("Largura da parede: "))
alt= float(input("Altura da parede: "))
area= lar * alt

print("A sua parede tem a dimensão de  {} x {} e sua aréa é de {}m².".format(lar, alt, area))
print("Para pintar essa parede, será necessário de {:.2f}L de tinta".format(area / 2))