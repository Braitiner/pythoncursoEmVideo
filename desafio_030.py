# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

from random import randint

num = randint(1,100)
resto = num % 2
if resto == 1:
    print('O numero: {} é IMPAR'.format(num))
else:
    print('O numero: {} é PAR'.format(num))
