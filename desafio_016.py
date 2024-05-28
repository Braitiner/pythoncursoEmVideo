# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
    # Ex: Digite um número: 6.127
    # O número 6.127 tem a parte Inteira 6.

import math

num = float(input('Digite um número: '))
real = num // 1
real2 = math.floor(num)
print('O numero {} tem a parte Inteira {:.0f} usando a biblioteca math {}'.format(num, real, real2))