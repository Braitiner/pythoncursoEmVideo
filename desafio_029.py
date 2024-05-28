# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

from random import randint

velocidade = randint(0, 200)
if velocidade > 80:
    print('Você foi multado, você esta a {} acima do limite de velocidade, valor da multa é R$ {}'.format(velocidade-80, (velocidade-80)*7))