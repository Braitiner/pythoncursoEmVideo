# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
pc = int(randint(1,3))
jogador = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\n >>>   '))
while True:
    if pc == jogador:
        print('empate jogue novamente')
        pc = int(randint(1,3))
        jogador = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\n >>>   '))
    elif jogador == 1:
        if pc == 2:
            print('PC ganhou, você jogou pedra e ele papel, papel ganha de pedra')
            break
        elif pc == 3:
            print('Ganhou, você jogou pedra e PC tesoura, pedra ganha de tesoura')
            break
    elif jogador == 2:
        if pc == 3:
            print('PC ganhou, você jogou papel e ele tesoura, tesoura ganha papel')
            break
        elif pc == 1:
            print('Ganhou, você jogou papel e PC pedra, papel ganha de pedra')
            break
    elif jogador == 3:
        if pc == 1:
            print('PC ganhou, você jogou tesoura e ele pedra, pedra ganha de tesoura')
            break
        elif pc == 2:
            print('Ganhou, você jogou tesoura e Papel, tesoura ganha de papel')
            break