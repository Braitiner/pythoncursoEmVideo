# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0, com um apausa de 1 segundo entre eles.

from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('Feliz ano novo!!!!!!')