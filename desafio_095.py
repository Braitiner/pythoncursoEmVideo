# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

jogador = {}
jogadores = []

while True:
    jogador.clear()
    jogador = {'nome': input('Nome do Jogador: ')}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    lista = list()
    for i in range(partidas):
        gols = int(input(f'Quantos gols na partida {i+1}? '))
        lista.append(gols)
    jogador['gols'] = lista.copy()
    jogador['total'] = sum(lista)
    jogadores.append(jogador.copy())
    continua = str(input('Deseja cadastrar um novo jogador [S/N]'))
    if continua in 'Nn':
        break
print(f'{"Cod":^5}{"Nome":^10}{"Gols":^15}{"Total":>6}')
for i, v in enumerate(jogadores):
    print(f'{i+1:^5}{v["nome"]:^10}     {v["gols"]}{v["total"]:>6}')
print('-='*30)
while True:
    opcao = int(input('Mostrar dados de qual jogador?   (999 para parar)'))
    if opcao == 999:
        break
    print(f'Levantamento do jogador {jogadores[opcao-1]["nome"]}:')
    for i, v in enumerate(jogadores[opcao-1]['gols']):
        print(f'=> Na partida {i+1}, fez {v} gols.')
    print(f'Foi um total de {jogadores[opcao-1]["total"]} gols')
