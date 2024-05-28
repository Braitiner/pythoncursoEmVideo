# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

# Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

n = int(input('Numero: '))
fibo = int(0)
fibo_anterior = 1
while fibo <= n:
    print(' {} > '.format(fibo),end='')
    if fibo == 0:
        fibo += 1
        print(' {} > '.format(fibo),end='')
    else:
        fibo_proximo = fibo_anterior + fibo
        fibo_anterior = fibo
        fibo = fibo_proximo
