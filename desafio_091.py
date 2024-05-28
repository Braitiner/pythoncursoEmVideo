# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6), 
             'jogador2': randint(1, 6), 
             'jogador3': randint(1, 6), 
             'jogador4': randint(1, 6)}
print('Valores sorteados')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ganhadores = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
posicao = 1
print('Ranking dos jogadores')
for k, v in ganhadores.items():
    print(f'{posicao}º lugar: {k} com {v}')
    sleep(1)
    posicao += 1

