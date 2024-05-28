# Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, mostre:
# A Quantos numeros foram digitados
#B A lista de valores ordenada de forma descrecente
# C Se o valor 5 foi digitado e esta ou não na lista

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    sair = input('Deseja sair [S/N]').upper()
    if sair == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros, A lista em ordem reversa é {lista}',end=' ')
if 5 in lista:
    posicao  = lista.index(5)
    print(f'O valor 5 foi digitado e esta na posicao {posicao} da lista')
else:
    print('O valor 5 não foi digitado')