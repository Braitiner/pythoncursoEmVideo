# Cria um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor a o maior valor que estão na tupla.
from random import randint
tupla = ()

for i in range(0, 5):
    tupla_atual = ()
    tupla_atual = (randint(1,9),)
    tupla = tupla + tupla_atual
    del(tupla_atual)

maior = max(tupla)
menor = min(tupla)
print(f'tupla formada {tupla}\nMaior {maior}\nMenor {menor}')