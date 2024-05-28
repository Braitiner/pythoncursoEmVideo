# Crie um programa que leia vários números interios pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

stop = True
cont = 0
soma = 0
maior = int(0)
menor = int(0)
while stop:
    n = int(input('Digite um número: '))
    if menor == 0:
        menor = n
    cont += 1
    soma += n
    maior = max(maior, n)
    menor = min(menor, n)
    parada = str(input('Deseja continuar:\n[S]\n[N]\n >>>   ')).upper()
    if parada == 'N':
        stop = False
print('Media {}\nMaior {}\nMenor {}'.format((soma/cont), maior, menor))