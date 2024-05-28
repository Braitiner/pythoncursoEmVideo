# Faça um programa que leia um numero qualquer e mostre na tela a sua tabuada.

n = int(input('informe um número:'))
for i in range(1, 11, 1):
    print('{:<3} x   {:<3} =   {:<3}'.format(n, i, n*i))