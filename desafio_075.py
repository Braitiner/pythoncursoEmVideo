# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A Quantas vezes apareceu o valor 9
# B Em que posição foi digitado o primeiro valor 3.
# C Quais foram os numeros pares

tupla = (int(input('N1 ')), int(input('N2 ')), int(input('N3 ')), int(input('N4 ')))
print(f'Nove apareceu {tupla.count(9)}\nPrimeiro 3 é na posição {tupla.index(3)}\nNumeros pares',end=' ')
for p in tupla:
    if p % 2 == 0:
        print(f'{p}',end=' ')