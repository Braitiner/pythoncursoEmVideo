# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estruta while.

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
cont = 10
while cont > 0:
    print(termo)
    termo += razao
    cont -= 1