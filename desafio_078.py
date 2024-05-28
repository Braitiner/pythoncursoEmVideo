# Faça u, prorgama que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for i in range(0, 5):
    lista.append(int(input('Informe um Numero: ')))
print(f'Maior valor foi {max(lista)} na posição {lista.index(max(lista))} da lista\nMenor valor foi {min(lista)} na posição {lista.index(min(lista))} da lista')
