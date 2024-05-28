# Dexsenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar desconsidere
soma = 0
for i in range(0,6):
    n = int(input('informe um numero: '))
    if (n%2) == 0:
        soma += n
print('A soma dos valores pares é {}'.format(soma))