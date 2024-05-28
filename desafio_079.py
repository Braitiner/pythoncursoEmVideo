# Crie um progrma onde o usuario possa criar vários valores numéricos e cadastre-os em uma lista. Caso o numero já exista lá dentro, ele não sera adicionado. No final, serão exibidos todos os valores únicos, em ordem crescente.

lista = []
while True:
    n = int(input('Digite um valor: '))
    sair = input('Deseja sair [S/N]').upper()
    if n not in lista:
        lista.append(n)
    if sair == 'N':
        break
lista.sort()
print(lista)