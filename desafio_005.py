#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Numero: '))
print('Antecessor de {} é {}'.format(n, n-1), end=' >>> ')
print('\nSucessor de {} é {}'.format(n, (n+1)))