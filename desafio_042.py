# refatore o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilatero: todos os lados iguais
#isoceles: dois lados iguais
# Escaleno: todos os lados diferentes

from random import randint

r1 = randint(1,6)
r2 = randint(1,6)
r3 = randint(1,6)

if (r1+r2) > r3 and (r2+r3) > r1 and (r1+r3) > r2:
    print('É um triangulo')
    if r1 == r2 and r1 == r3:
        print('Equilatero')
    elif r1 == r2 or r1 == r3:
        print('Isoceles')
    else:
        print('Escaleno')
else:
    print('Não é um triangulo')