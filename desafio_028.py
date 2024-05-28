# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuario venceu ou perdeu

import random

num = random.randint(0,5)
print(num)
chute = int(input("numero de 0 a 5: "))
if num == chute: 
    print('Venceu')
else:
    print('perdeu, o numero era {}'.format(num))
