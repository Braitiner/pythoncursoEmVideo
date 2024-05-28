# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#EX: 5x4x3x2x1 = 120

n = int(input('Numero: '))
fatorial = 1
print('{}! = '.format(n),end='')
while n > 0:
    fatorial *= n
    if n == 1:
        print('{} '.format(n),end='')
    else:
        print('{} X '.format(n),end='')
    n -= 1
print('= {}'.format(fatorial))

