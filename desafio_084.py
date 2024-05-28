# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    # A) Quantas pessoas foram cadastradas.
    # B) Uma listagem com as pessoas mais pesadas.
    # C) Uma listagem com as pessoas mais leves.

lista = list()
auxiliar = list()
mais_pesadas = list()
mais_leves = list()

# Adiciona as pessoas a lista usando a auxiliar para input de dados, sai do loop quando o usuario informar N.
while True:
    auxiliar.append(str(input('Nome: ')))
    auxiliar.append(float(input('Peso: ')))
    lista.append(auxiliar[:])
    auxiliar.clear()
    if str(input('Novo cadastro [S/N] ')).upper() == 'N':
        break

# Verifica quais pessoas é mais leves e pesadas guardando nas listas, foi usado o key=lambda para definir que o valor que max e min vai olhar é o peso que esta em [1]
pesadas = max(lista, key=lambda x: x[1])
leves = min(lista, key=lambda x: x[1])
for i in lista:
    if  i[1] == pesadas[1]:
        mais_pesadas.append(i[0])
    if i[1] == leves[1]:
        mais_leves.append(i[0])

#Realiza a impressao no terminal utilizando o for para imprimir os nomes
print(f"Ao todo você cadastrou {len(lista)} pessoas")
print(f'O maior peso foi de {pesadas[1]} Kg. Peso de', end=' ')
for i in mais_pesadas:
    print(f'[{i}]', end=' ')
print(f'\nO menor peso foi de {leves[1]} Kg. Peso de', end=' ')
for i in mais_leves:
    print(f'[{i}]', end=' ')
