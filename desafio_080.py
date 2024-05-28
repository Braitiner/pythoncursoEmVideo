# Crie um programa onde o usuario possa digitar cinco valores númericos e cadastr-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# no final, mostre a lista ordenada na tela.

lista = []
menor = maior = 0
for i in range(5):
    n = int(input('Numero: '))
    if i == 0:
        lista.insert(i, n)
        menor = maior = n
    else:
        if n <= menor:
            lista.insert(0, n)
            menor = n
        elif n >= maior:
            lista.insert(i, n)
            maior = n
        else:
            if i == 2:
                lista.insert(1, n)
            elif i == 3:
                if n >= lista[1]:
                    lista.insert(2, n)
                elif n <= lista[1]:
                    lista.insert(1, n)
            elif i == 4:
                if n >= lista[1]:
                    lista.insert(2, n)
                elif n >= lista[2]:
                    lista.insert(3, n)
                elif n <= lista[1]:
                    lista.insert(1, n)
                elif n <= lista[2]:
                    lista.insert(2, n)
print(lista)