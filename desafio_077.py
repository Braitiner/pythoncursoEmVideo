# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Papel', 'Celular', 'cabo', 'SSD')

for palavra in tupla:
    print(f'A palavar {palavra} tem as vogais ',end=' ')
    for i in palavra:
        if i.upper() in ('AEIOU'):
            print(i,end=' ')
    print('\n')