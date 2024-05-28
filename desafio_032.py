# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from random import randint

ano = randint(1,3600)
restoMultiploDeQuatro = ano % 4
restoMultiploDeCem = ano % 100
restoMultiploDeQuatrocentos = ano % 400
if restoMultiploDeQuatro == 0:
    if restoMultiploDeCem == 0:
        if restoMultiploDeQuatrocentos == 0:
            print('O ano {} é bissexto'.format(ano))
        else:
            print('O ano {} não é bissexto'.format(ano))
    else:
            print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
     
