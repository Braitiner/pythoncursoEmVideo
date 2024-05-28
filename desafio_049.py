# refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher, so que agora utilizando um laço for.print

n = int(input('Qual tabuada quer ver: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(i, n, i*n)) 