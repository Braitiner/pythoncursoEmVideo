# Melhore o desafio 61, pergunte para o usuario se ele quer mostrar mais alguns termos. O prorgama encerra quando ele disser que quer mostrar 0 termos.

continua = 1
while continua != 0:
    termo = int(input('Informe o primeiro termo: '))
    razao = int(input('Informe a razao: '))
    cont = 10
    while cont > 0:
        print(termo)
        termo += razao
        cont -= 1
    continua = int(input('[0] - Sair\n[1] continua'))
