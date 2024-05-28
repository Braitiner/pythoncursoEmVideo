# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar.

n = float(input('Quanto tem de dinheiro R$: '))
print('Você pode comprar US${:.2f} com seus R$ {:.2f}'.format(n/4.9, n))