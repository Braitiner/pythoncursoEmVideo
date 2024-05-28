# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import datetime

ano_atual = datetime.now().year
maior = 0
menor = 0
for i in range(0,7):
    ano_nascimento = int(input('Ano nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Maior de idade: {}\nMenor de idade: {}'.format(maior, menor))
