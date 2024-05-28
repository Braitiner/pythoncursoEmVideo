# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

j = 0

while True:
    pc = randint(0, 5)
    player = int(input('Par ou Impar\n1 para par\n2 para Impar\n >>>>   '))
    n = int(input('Qual Numero vai jogar, escolha de 0 a 5\n >>>>'))
    if player == 1:
        if (pc + n) % 2 == 0:
            print(f'Par ganhou!!!! PC jogou {pc} Você jogou {n}\n\n' )
            j += 1
        else:
            break
    elif player == 2:
        if (pc + n) % 2 == 1:
            print(f'Impar ganhou!!!! PC jogou {pc} Você jogou {n}\n\n' )
            j += 1
        else:
            break
print(f'Perdeu!!!! PC jogou {pc} Você jogou {n}, você ganhou {j} jogos\n\n' )
