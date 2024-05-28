# Faça um programa que ajude um jogador da mega sena a criar palpites. 
# O programa vai perguntar quantos quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista_apostas = []
temp = []
apostas = int(input('Quantos jogos quer realizar: '))

for i in range(0, apostas):
    for s in range(0, 6):
        while True:
            numero = randint(1, 60)
            if numero not in temp:
                temp.append(numero)
                break
    lista_apostas.append(sorted(temp[:]))
    temp.clear()
for i, j in enumerate(lista_apostas):
    print(f'Jogo {i+1}: {j}')
    sleep(0.5)