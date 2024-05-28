# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acetar, 
# mostrando no final quantos palpites foram necessarios

import random

num = random.randint(0,10)
chute = int(-1)
count = 0
# print(num)
while chute != num:
    chute = int(input("numero de 0 a 10: "))
    if num == chute: 
        print('Venceu')
    count += 1
print('Quantidade de chutes: {}'.format(count))