# Faça um prorgama que leia um número inteiro e diga se ele é ou não um número primo

n = int(input('Numero: '))
primo = 0
for i in range(2, n+1):
    div = n % i
    if div == 0:
        primo += 1
    if primo == 1 and i == n:
        print('numero primo')
    elif primo != 1 and i == n:
        print('Não é primo')