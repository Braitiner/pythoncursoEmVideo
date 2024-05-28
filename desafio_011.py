# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para printa-la, 
# sabendo que cada litro de tinta pinta uma area de 2m²

l = float(input('Informe a largura: '))
a = float(input('Informe a altura: '))
print("a metragem quadrada para pintura é de {}m² você vai precisar de {} litros de tinta".format(l*a,(l*a)/2))