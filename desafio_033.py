# Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor

from random import randint

n1 = randint(0,100)
n2 = randint(0,100)
n3 = randint(0,100)
if n1 > n2 and n1 > n3:
    print('{} maior'.format(n1))
    if n2 > n3:
        print('{} menor'.format(n3))
    else:
        print('{} menor'.format(n2))
else:
    if n2 > n3:
        print('{} maior'.format(n2))
        if n1 > n3:
            print('{} menor'.format(n3))
        else:
            print('{} menor'.format(n1))
    else:
        print('{} maior'.format(n3))
        if n1 > n2:
            print('{} menor'.format(n2))
        else:
            print('{} menor'.format(n1))




