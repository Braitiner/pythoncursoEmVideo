# Faça um programa que leia um número de 0 a 9999 e mosttre na tela cada um dos digitos separados
# Ex: Digite um número? 1834
# Unidade:4
# Dezena:3
# centena:8
# milhar:1

numeroStrint = input('Digite um número: ')
numeroStrint = ' '.join(str(numeroStrint).zfill(4))
print('Unidades: {:3}\nDezena: {:3}\nCentena: {:3}\nMilhar: {:3}'.format(numeroStrint.split()[3],numeroStrint.split()[2],numeroStrint.split()[1],numeroStrint.split()[0]))