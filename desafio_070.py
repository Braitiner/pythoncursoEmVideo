# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar. No final mostre
# A qual o total gasto na compra
# B Quantos produtos custam mais de R$ 1000
# C Qual é o nome do produto mais barato

total = caros = preco = 0 
nome_barato = ''
barato = float('inf')
while True:
    print('\n\nPreencha >>>')
    produto = str(input('Produto: '))
    preco = int(input('Preço: '))
    total += preco
    if preco > 1000:
        caros += 1
    barato = min(barato, preco)
    if preco == barato:
        nome_barato = produto
    continua = str(input('Adiciona mais produto [S/N]  ')).upper()
    if continua == 'N':
        break
print(f'Total: {total}\nCaros: {caros}\nBaratim: {nome_barato}')