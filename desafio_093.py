# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quatas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso sera guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {'nome': input('Nome do Jogador: ')}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
lista = list()
for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    lista.append(gols)
jogador['gols'] = lista.copy()
jogador['total'] = sum(lista)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas}. partidas')
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')

