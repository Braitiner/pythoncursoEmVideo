# Crie um programa que vai ler vários números e colocar em uma lista.

#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente.

# Ao final, mostre o conteudo das tres listas gerdas.

lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    sair = input('Deseja sair [S/N]').upper()
    if sair == 'N':
        break
for p in lista:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)

print(f'Lista {lista}\n Lista par {par}\nLista impar {impar}')
