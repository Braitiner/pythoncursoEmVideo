# Desenvolva um progama que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.

from random import randint

r1 = randint(1,6)
r2 = randint(1,6)
r3 = randint(1,6)

if (r1+r2) > r3 and (r2+r3) > r1 and (r1+r3) > r2:
    print('É um triangulo')
else:
    print('Não é um triangulo')