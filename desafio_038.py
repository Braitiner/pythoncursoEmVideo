# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
# - O primeiro valor é maior
# - O segundo valor é maior
# - O Não existe valor maior os dois são iguais

from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)

if n1 > n2: 
    print('O primero numero {} é maior que o segudno {}'.format(n1,n2))
elif n2 > n1: 
    print('O segundo numero {} é maior que o primeiro {}'.format(n2,n1))
elif n1 == n2:
    print('O primero numero {} é igual ao segudno {}'.format(n1,n2))
