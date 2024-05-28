# Desenvolva um programa que pergunte a dustancia de uma viagem em km.
# Calcule o preço da passagem,cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.

from random import randint

distancia = randint(35,1850)
if distancia > 200:
    print('o preço da passagem de {} km é R$ {:.2f}'.format(distancia, distancia*0.45))
else:
    print('o preço da passagem de {} km é R$ {:.2f}'.format(distancia, distancia*0.50))
