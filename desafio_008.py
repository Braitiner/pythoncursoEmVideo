#Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimitros

n = float(input("Metros: "))
print('Centimetros: {:.2f} c\nMilimitros: {:.2f} mm'.format(n*100, n*1000))